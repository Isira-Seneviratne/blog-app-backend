from pydantic import BaseSettings


class Settings(BaseSettings):
    """A class containing the environment variables of the application."""
    database_url: str = "sqlite:///sql_app.db"


settings = Settings()
