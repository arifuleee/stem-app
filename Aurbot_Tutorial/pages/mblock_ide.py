import reflex as rx
from ..ui.base import base_page

def mblock_ide_page() -> rx.Component:
    return base_page(
        rx.html(
            """
            <iframe src="https://ide.mblock.cc/" width="100%" height="1000px" frameborder="0"></iframe>
            """
        )
    )
