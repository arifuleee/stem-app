# full_stack_python/pages/course_detail.py

import reflex as rx
from ..ui.base import base_page
from .state import CourseState, ReviewState

def review_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(name="rating", type="number", min="1", max="5", placeholder="Rating (1-5)"),
            rx.text_area(name="comment", placeholder="Write your review..."),
            rx.button("Submit", type="submit"),
        ),
        on_submit=ReviewState.add_review
    )

def course_detail_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading(CourseState.current_course.title, size="9"),
            rx.text(CourseState.current_course.description),
            rx.video(
                controls=True,
                width="100%",
                height="auto",
                src=CourseState.current_course.video_url
            ),
            review_form(),
            spacing="5",
            align="center",
            min_height="85vh"
        )
    )

