# TODO: Feature 2
from src.models.movie import Movie
from tests.unit.test_movie_model import test_movie_model

resources = Movie(__file__).parent




def test_create_movie():
    assert test_movie_model
    response = client.post("/movies", follow_redirects=True, data={
        'title' == 'Star Wars'
        'director' == 'George Lucas'
        'rating' == 5
    })
    assert response.status_code == 200