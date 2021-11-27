from fastapi import FastAPI, status

from src.apis.blog_post_apis import blog_post_router
from src.schemas import Base, engine

app = FastAPI()
app.include_router(blog_post_router)

Base.metadata.create_all(bind=engine)


@app.get('/')
def index():
    """The root route which returns a basic JSON response.

    :return: A JSON response containing 'Hello world!'.
    """
    return {'message': 'Hello world!'}


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_health_check():
    """Simple route for the GitHub Actions to health check on.

    More info is available at: https://github.com/akhileshns/heroku-deploy#health-check

    :return: A response indicating that the server is up and running.
    """
    return {'healthcheck': 'Everything OK!'}
