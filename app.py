import re
from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()

form_data = {}


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2 - COMPLETE
    # After creating the movie in the database, we redirect to the list all movies page
    movie_repository.create_movie(request.form.get('movie'), request.form.get('director'), request.form.get('rating'))

#if the movie repository isn't working, uncomment the 3 lines below and use that instead.
    #movie = request.form.get('movie')
    #details = [ request.form.get('director'), request.form.get('rating') ]
    #form_data[movie] = details

    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
