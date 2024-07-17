import reflex as rx
# from ..auth.state import SessionState
from .sidebar import sidebar


def base_layout_component(child, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                padding="1em",
                width="100%",
                id="my-content-area-el"
            ),
        ),
        rx.color_mode.button(position="bottom-left"),
    )


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("this is not a valid child element")
    return base_layout_component(child, *args, **kwargs)
