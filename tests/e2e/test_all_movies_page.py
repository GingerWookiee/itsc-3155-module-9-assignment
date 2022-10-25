# TODO: Feature 1
from flask.testing import FlaskClient


def test_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data

    assert b' <th>Movie Title</th>' in response_data
    assert b' <th>Director</th>' in response_data
    assert b' <th>Rating</th>' in response_data