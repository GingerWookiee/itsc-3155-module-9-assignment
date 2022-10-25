# TODO: Feature 3
from src.models.movie import Movie
from app import movie_repository
from src.repositories.movie_repository import get_movie_repository

def get_movie_test():
    movie_repository.create_movie("title1","director1",3)
    movie = movie_repository.get_movie_by_title("title1")
    assert movie