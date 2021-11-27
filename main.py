from fastapi import FastAPI, status

app = FastAPI()


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
