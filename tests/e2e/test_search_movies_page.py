# TODO: Feature 3
from flask.testing import FlaskClient


def test_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/search_movies.html')
    response_data = response.data

    assert b'<tr><th>Movie Title</th><th>Director</th><th>Rating</th></tr>' in response_data
