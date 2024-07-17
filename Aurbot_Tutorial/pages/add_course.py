import reflex as rx
from ..ui.base import base_page
from .state import CourseState

def add_course_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(name="title", placeholder="Course Title", required=True),
            rx.text_area(name="description", placeholder="Course Description", required=True),
            rx.input(name="youtube_link", placeholder="YouTube Video Link", required=True),
            rx.button("Add Course", type="submit"),
        ),
        on_submit=CourseState.add_course,
        method="post",
        enc_type="application/x-www-form-urlencoded"
    )

def add_course_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Add Course", size="9"),
            add_course_form(),
            spacing="5",
            align="center",
            min_height="85vh"
        )
    )

# import reflex as rx
# from ..ui.base import base_page
# from .state import CourseState

# def add_course_form() -> rx.Component:
#     return rx.form(
#         rx.vstack(
#             rx.input(name="title", placeholder="Course Title", required=True),
#             rx.text_area(name="description", placeholder="Course Description", required=True),
#             rx.input(name="youtube_link", placeholder="YouTube Link", required=True),
#             rx.button("Add Course", type="submit"),
#         ),
#         on_submit=CourseState.add_course
#     )

# def add_course_page() -> rx.Component:
#     return base_page(
#         rx.vstack(
#             rx.heading("Add Course", size="9"),
#             add_course_form(),
#             spacing="5",
#             align="center",
#             min_height="85vh"
#         )
#     )
