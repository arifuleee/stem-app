from datetime import datetime
from typing import Optional, List
import reflex as rx
from sqlmodel import select

import os
from openai import AsyncOpenAI

from ..auth.state import SessionState
from ..models import CourseModel, ReviewModel

class CourseState(SessionState):
    courses: List[CourseModel] = []
    current_course: Optional[CourseModel] = None

    @rx.var
    def course_id(self):
        return self.router.page.params.get("course_id", "")

    def load_courses(self):
        with rx.session() as session:
            self.courses = session.exec(select(CourseModel)).all()
            self.courses = [course.to_dict() for course in self.courses]  # Ensure serialization

    def load_course_detail(self):
        if not self.course_id:
            return
        with rx.session() as session:
            self.current_course = session.exec(select(CourseModel).where(CourseModel.id == self.course_id)).one_or_none()
            if self.current_course:
                self.current_course = self.current_course.to_dict()  # Ensure serialization

    def add_course(self, form_data):
        print("Form Data Received:", form_data)  # Debugging print

        title = form_data.get('title')
        description = form_data.get('description')
        youtube_link = form_data.get('youtube_link')

        if youtube_link:
            new_course = CourseModel(title=title, description=description, video_url=youtube_link)
            with rx.session() as session:
                session.add(new_course)
                session.commit()
                session.refresh(new_course)  # Ensure the new_course is fully loaded
                self.courses.append(new_course.to_dict())  # Convert to dict to avoid DetachedInstanceError
        else:
            print("Invalid YouTube link data received.")  # Debugging print

    def enroll_in_course(self, course_id):
        print(f"Enrolled in course with ID: {course_id}")





class ReviewState(SessionState):
    reviews: List[ReviewModel] = []
    current_course_id: Optional[int] = None

    def load_reviews(self):
        if not self.current_course_id:
            return
        with rx.session() as session:
            self.reviews = session.exec(select(ReviewModel).where(ReviewModel.course_id == self.current_course_id)).all()

    def add_review(self, form_data):
        rating = int(form_data.get('rating', 0))
        comment = form_data.get('comment', '')
        new_review = ReviewModel(user_id=self.my_user_id, course_id=self.current_course_id, rating=rating, comment=comment)
        with rx.session() as session:
            session.add(new_review)
            session.commit()
            self.reviews.append(new_review)

class TutorialState(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []

    async def answer(self):
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
        session = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.question}],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        answer = ""
        self.chat_history.append((self.question, answer))
        self.question = ""
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield
