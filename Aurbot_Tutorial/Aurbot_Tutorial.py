import reflex as rx
import reflex_local_auth

from rxconfig import config
from .ui.base import base_page

from .auth.pages import (
    my_login_page,
    my_register_page,
    my_logout_page
)
from .auth.state import SessionState

from .articles.detail import article_detail_page
from .articles.list import article_public_list_page, article_public_list_component
from .articles.state import ArticlePublicState

from . import blog, contact, navigation, pages
from .pages.course_detail import course_detail_page
from .pages.dashboard import dashboard_component
from .pages.landing import landing_component
from .pages.state import CourseState
from .pages.add_course import add_course_page
from .pages.courses import courses_page  # Import the courses page
from .pages.chatapp import aurobot_page  # Import the chatbot page
from .pages.python_ide import python_ide_page  # Import the Python IDE page
from .pages.mblock_ide import mblock_ide_page  # Import the mBlock IDE page

def index() -> rx.Component:
    return base_page(
        rx.cond(
            SessionState.is_authenticated,
            dashboard_component(),
            landing_component()
        )
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        panel_background="solid",
        scaling="90%",
        radius="medium",
        accent_color="sky"
    )
)

app.add_page(index, on_load=ArticlePublicState.load_posts)

app.add_page(my_login_page, route=reflex_local_auth.routes.LOGIN_ROUTE, title="Login")
app.add_page(my_register_page, route=reflex_local_auth.routes.REGISTER_ROUTE, title="Register")
app.add_page(my_logout_page, route=navigation.routes.LOGOUT_ROUTE, title="Logout")

app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(pages.protected_page, route="/protected/", on_load=SessionState.on_load)
app.add_page(article_public_list_page, route=navigation.routes.ARTICLE_LIST_ROUTE, on_load=ArticlePublicState.load_posts)
app.add_page(article_detail_page, route=f"{navigation.routes.ARTICLE_LIST_ROUTE}/[post_id]", on_load=ArticlePublicState.get_post_detail)

app.add_page(blog.blog_post_list_page, route=navigation.routes.BLOG_POSTS_ROUTE, on_load=blog.BlogPostState.load_posts)
app.add_page(blog.blog_post_add_page, route=navigation.routes.BLOG_POST_ADD_ROUTE)
app.add_page(blog.blog_post_detail_page, route="/blog/[blog_id]", on_load=blog.BlogPostState.get_post_detail)
app.add_page(blog.blog_post_edit_page, route="/blog/[blog_id]/edit", on_load=blog.BlogPostState.get_post_detail)

app.add_page(contact.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(contact.contact_entries_list_page, route=navigation.routes.CONTACT_ENTRIES_ROUTE, on_load=contact.ContactState.list_entries)
# app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)

app.add_page(course_detail_page, route="/course/[course_id]", on_load=CourseState.load_course_detail)
app.add_page(courses_page, route=navigation.routes.COURSES_ROUTE, on_load=CourseState.load_courses)  # Add the courses page
app.add_page(dashboard_component, route="/dashboard", on_load=CourseState.load_courses)
app.add_page(add_course_page, route=navigation.routes.ADD_COURSE_ROUTE)

app.add_page(aurobot_page, route=navigation.routes.AUROBOT_ROUTE)  # Add the AuroBot page
app.add_page(python_ide_page, route=navigation.routes.PYTHON_IDE_ROUTE)  # Add the Python IDE page
app.add_page(mblock_ide_page, route=navigation.routes.MBLOCK_IDE_ROUTE)  # Add the mBlock IDE page

