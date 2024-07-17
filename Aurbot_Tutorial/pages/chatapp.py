import reflex as rx

from .style import question_style, answer_style, input_style, button_style
from .state import TutorialState
from ..ui.base import base_page


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=answer_style,
        ),
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            TutorialState.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
        height="80vh",  # Adjust height to fit within the page
        overflow="auto",  # Add scroll if messages exceed the height
        padding="1em",  # Add padding for better spacing
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            value=TutorialState.question,
            on_change=TutorialState.set_question,
            style=input_style,
        ),
        rx.button(
            "Ask",
            on_click=TutorialState.answer,
            style=button_style,
        ),
        width="100%",  # Ensure it spans the full width of the container
        spacing="1em",  # Add spacing between input and button
    )


def aurobot_page() -> rx.Component:
    return base_page(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
            spacing="1em",  # Add spacing between chat and action bar
            padding="1em",  # Add padding for better layout
        )
    )


# Your app initialization should include the aurobot_page
# app = rx.App()
# app.add_page(aurobot_page, route="/aurobot")
