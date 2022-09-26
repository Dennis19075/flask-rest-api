import json
from platform import release
from flask import Blueprint, jsonify, request
import uuid

#Entities
from models.entities.Movie import Movie

#Models 
from models.MovieModel import MovieModel

main =  Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_movie():
    try:
        # print(request.json)
        title = request.json['title']
        duration = request.json['duration']
        released = request.json['released']
        id = uuid.uuid4()
        print(type(id))
        print(type(str(id)))
        movie = Movie(str(id), title, duration, released)
        print(movie)
        affected_rows = MovieModel.add_movie(movie)
        if affected_rows == 1:
            return jsonify(movie.id)
        else: 
            return jsonify({'message': 'Error on insert'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500