from src.schemas import SessionLocal


def get_db():
    """Creates a DB instance. This is for use with FastAPI's dependency injection functionality.

    :return: A DB instance.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
