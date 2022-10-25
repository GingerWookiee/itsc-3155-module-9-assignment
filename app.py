from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()

# hard-coded test code - comment out later
movie_repository.create_movie('title1', 'director1', 1)
movie_repository.create_movie('title2', 'director2', 2)
movie_repository.create_movie('title3', 'director3', 3)
movie_repository.create_movie('title4', 'director4', 4)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    movie = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movie = movie)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    movie_repository.create_movie(request.form.get('title'), request.form.get('director'), request.form.get('rating'))
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
