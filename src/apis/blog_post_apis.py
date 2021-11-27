from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.schemas.request_schemas import BlogPostBase, BlogPost
from src.services import blog_post_service
from . import get_db

blog_post_router = APIRouter()


@blog_post_router.post('/blogPost', response_model=BlogPost)
def create_blog_post(blog_post: BlogPostBase, db: Session = Depends(get_db)):
    """Creates a blog post using the provided JSON payload.

    :param blog_post: The blog post.
    :param db: The DB session (this is automatically injected).
    :return: The newly-created blog post.
    """
    return blog_post_service.create_blog_post(db, blog_post)


@blog_post_router.patch('/blogPost', response_model=BlogPost)
def update_blog_post(blog_post: BlogPost, db: Session = Depends(get_db)):
    """Updates an existing blog post using the provided JSON payload.

    :param blog_post: The blog post.
    :param db: The DB session (this is automatically injected).
    :return: The updated blog post.
    """
    blog_post = blog_post_service.update_blog_post(db, blog_post)
    if not blog_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog post not found')
    return blog_post


@blog_post_router.delete('/blogPost', response_model=BlogPost)
def delete_blog_post(post_id: int, db: Session = Depends(get_db)):
    """Deletes an existing blog post with the given ID.

    :param post_id: The blog post ID.
    :param db: The DB session (this is automatically injected).
    :return: The deleted blog post.
    """
    blog_post = blog_post_service.delete_blog_post(db, post_id)
    if not blog_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog post not found')
    return blog_post


@blog_post_router.get('/getAllBlogPosts', response_model=list[BlogPost])
def get_all_blog_posts(db: Session = Depends(get_db)):
    """Returns all the blog posts stored in the database (limited to 100 by default).

    :param db: The DB session (this is automatically injected).
    :return: The list of blog posts stored in the DB.
    """
    return blog_post_service.get_all_blog_posts(db)
