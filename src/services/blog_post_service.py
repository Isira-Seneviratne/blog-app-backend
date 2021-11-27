from __future__ import annotations

from sqlalchemy.orm import Session

from src.schemas import request_schemas, database_schemas


def create_blog_post(db: Session, blog_post: request_schemas.BlogPostBase) -> database_schemas.BlogPost:
    """Creates a new blog post.

    :param db: The database session.
    :param blog_post: The blog post to be created.
    :return: The newly-created blog post.
    """
    db_blog_post = database_schemas.BlogPost(title=blog_post.title, body=blog_post.body)
    db.add(db_blog_post)
    db.commit()
    db.refresh(db_blog_post)
    return db_blog_post


def update_blog_post(db: Session, blog_post: request_schemas.BlogPost) -> database_schemas.BlogPost | None:
    """Updates an existing blog post.

    :param db: The database session.
    :param blog_post: The blog post to be updated.
    :return: The updated blog post.
    """
    db_blog_post = db.query(database_schemas.BlogPost).get(blog_post.id)
    if not db_blog_post:
        return None
    for key, value in blog_post.dict(exclude={'id'}).items():
        setattr(db_blog_post, key, value)
    db.commit()
    return db_blog_post


def delete_blog_post(db: Session, post_id: int) -> database_schemas.BlogPost | None:
    """Deletes the blog post with the given ID if it already exists.

    :param db: The database session.
    :param post_id: The blog post ID to be deleted.
    :return: The deleted blog post.
    """
    db_blog_post = db.query(database_schemas.BlogPost).get(post_id)
    if not db_blog_post:
        return None
    db.delete(db_blog_post)
    db.commit()
    return db_blog_post


def get_all_blog_posts(db: Session, limit: int = 100) -> list[database_schemas.BlogPost]:
    """Gets all the blog posts saved in the DB.

    :param db: The database session.
    :param limit: The maximum no. of records to be obtained (default is 100).
    :return: A list of blog posts.
    """
    return db.query(database_schemas.BlogPost).limit(limit).all()
