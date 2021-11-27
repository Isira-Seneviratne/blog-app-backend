from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class BlogPost(Base):
    """The ORM representation of a blog post."""
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100))
    body = Column(String)

    comments = relationship("Comment", cascade="all,delete")


class Comment(Base):
    """The ORM representation of a comment on a blog post."""
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    blog_post_id = Column(Integer, ForeignKey("blog_posts.id"))
