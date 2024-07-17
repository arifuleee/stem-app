# full_stack_python/pages/courses.py

import reflex as rx
from ..ui.base import base_page
from .state import CourseState

def course_list_item(course) -> rx.Component:
    return rx.chakra.tr(
        rx.chakra.td(course.title),
        rx.chakra.td(course.description),
        rx.chakra.td(rx.link("Watch on YouTube", href=course.video_url, target="_blank")),
        rx.chakra.td(rx.button("Enroll", on_click=lambda: CourseState.enroll_in_course(course.id)))
    )
def courses_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Available Courses", size="9"),
            rx.chakra.table_container(
                rx.chakra.table(
                    rx.chakra.thead(
                        rx.chakra.tr(
                            rx.chakra.th("Title"),
                            rx.chakra.th("Description"),
                            rx.chakra.th("Video Link"),
                            rx.chakra.th("Action")
                        )
                    ),
                    rx.chakra.tbody(
                        rx.foreach(CourseState.courses, course_list_item)
                    )
                )
            ),
            spacing="5",
            align="center",
        )
    )