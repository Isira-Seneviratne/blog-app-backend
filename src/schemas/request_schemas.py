from pydantic import BaseModel


class Comment(BaseModel):
    """The schema for a comment."""
    body: str


class BlogPostBase(BaseModel):
    """The schema for a blog post (DB properties such as ID and comments are not included here.)"""
    title: str
    body: str


class BlogPost(BlogPostBase):
    """The schema for a blog post as returned from the REST API."""
    id: int

    class Config:
        orm_mode = True
