# full_stack_python/pages/landing.py

import reflex as rx

def landing_component() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome to the Learning Platform", size="9"),
        rx.text("Sign up or log in to access the courses."),
        rx.link(
            rx.button("Sign Up", color_scheme="blue"),
            href="/register"
        ),
        rx.link(
            rx.button("Log In", color_scheme="blue"),
            href="/login"
        ),
        spacing="5",
        align="center",
        min_height="85vh"
    )


""" import reflex as rx 

from .. import navigation
from ..articles.list import article_public_list_component


def landing_component() -> rx.Component:
    return rx.vstack(
            # rx.theme_panel(default_open=True),
            # rx.heading("Welcome to SaaS", size="9"),
                rx.flex(
                    rx.flex(
                        rx.text("Learn to code! Try new challenges and have fun!", as_ = "p",
                                weight = 'bold', 
                                size = '9', 
                                text_align = 'center',
                            ),
                            rx.text("Get started by trying a programming language in the playground!", 
                                    text_align = 'center',),
                                rx.button(
                                "Check the playground!",
                                on_click = lambda: rx.redirect("/playground"), 
                                width = '40%',
                                text_align = 'center',
                                padding = '2rem',
                                margin_top = '2rem',
                                ),
                        width = ['100%','100%','100%','80%','60%'],
                        margin_top = 'auto',
                        margin_bottom = 'auto',
                        direction = 'column',
                        align = 'center',
                        ),
                        rx.desktop_only(
                        rx.avatar(
                                src = '/aurbotlogo.jpeg', 
                                width = '80%',
                                height = 'auto',
                                margin_top = 'auto',
                                margin_bottom = 'auto',
                                border_radius="25%",
                        ),
                        width = '40%',
                        ),
                        width = '100%',
                        padding = '2rem',
                        margin = "1rem",
                        direction = 'row',
                        align = 'center',
                    ), 
            rx.link(
                rx.button("About us", color_scheme='gray'), 
                href=navigation.routes.ABOUT_US_ROUTE
            ),
            rx.divider(),
            rx.heading("Recent Articles", size="5"),
            article_public_list_component(columns=1, limit=1),
            spacing="5",
            justify="center",
            align="center",
            # text_align="center",
            min_height="85vh",
            id='my-child'
        ) """