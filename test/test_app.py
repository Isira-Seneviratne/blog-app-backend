from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_index():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world!'}


def test_perform_health_check():
    response = client.get('/healthcheck')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'healthcheck': 'Everything OK!'}
