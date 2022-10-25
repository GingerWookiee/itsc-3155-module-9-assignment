# TODO: Feature 1
from src.models.movie import Movie

def movie_exists():
    movie = Movie('The Notebook', 'Nick Cassavetes', 8)

    assert type(movie) == Movie
    assert movie.title == 'The Notebook'
    assert movie.director == 'Nick Cassavetes'
    assert movie.rating == 8