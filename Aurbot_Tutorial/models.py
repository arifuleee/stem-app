# full_stack_python/utils/models.py

from typing import Optional, List
from datetime import datetime
import reflex as rx
from reflex_local_auth.user import LocalUser

import sqlalchemy
from sqlmodel import Field, Relationship, SQLModel

from . import utils

class UserInfo(rx.Model, table=True):
    email: str
    user_id: int = Field(foreign_key='localuser.id')
    user: LocalUser | None = Relationship()  # LocalUser instance
    posts: List['BlogPostModel'] = Relationship(
        back_populates='userinfo'
    )
    contact_entries: List['ContactEntryModel'] = Relationship(
        back_populates='userinfo'
    )
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    role: str  # Add role field to UserInfo

# class UserInfo(rx.Model, table=True):
#     email: str
#     user_id: int = Field(foreign_key='localuser.id')
#     user: LocalUser | None = Relationship()  # LocalUser instance
#     posts: List['BlogPostModel'] = Relationship(
#         back_populates='userinfo'
#     )
#     contact_entries: List['ContactEntryModel'] = Relationship(
#         back_populates='userinfo'
#     )
#     created_at: datetime = Field(
#         default_factory=utils.timing.get_utc_now,
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'server_default': sqlalchemy.func.now()
#         },
#         nullable=False
#     )
#     updated_at: datetime = Field(
#         default_factory=utils.timing.get_utc_now,
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'onupdate': sqlalchemy.func.now(),
#             'server_default': sqlalchemy.func.now()
#         },
#         nullable=False
#     )


class BlogPostModel(rx.Model, table=True):
    userinfo_id: int = Field(default=None, foreign_key="userinfo.id")
    userinfo: Optional['UserInfo'] = Relationship(back_populates="posts")
    title: str
    content: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )
    publish_active: bool = False
    publish_date: datetime = Field(
        default=None,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={},
        nullable=True
    )


class ContactEntryModel(rx.Model, table=True):
    user_id: int | None = None
    userinfo_id: int = Field(default=None, foreign_key="userinfo.id")
    userinfo: Optional['UserInfo'] = Relationship(back_populates="contact_entries")
    first_name: str
    last_name: str | None = None
    email: str | None = None
    message: str
    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )


# class CourseModel(rx.Model, table=True):
#     title: str
#     description: str
#     video_url: str = ""
#     created_at: datetime = Field(default_factory=utils.timing.get_utc_now)
#     updated_at: datetime = Field(default_factory=utils.timing.get_utc_now)

# class CourseModel(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     title: str
#     description: str
#     youtube_link: str
class CourseModel(rx.Model, table=True):
    title: str
    description: str
    video_url: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'video_url': self.video_url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

class ReviewModel(rx.Model, table=True):
    user_id: int = Field(foreign_key='localuser.id')
    course_id: int = Field(foreign_key='coursemodel.id')
    rating: int
    comment: str
    created_at: datetime = Field(default_factory=utils.timing.get_utc_now)
