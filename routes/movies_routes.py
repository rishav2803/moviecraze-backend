from flask import Blueprint, request, jsonify
# from backend.models.user_model import User
from flask import Blueprint
from backend import db
from bson import json_util
import json
import uuid


movies_bp = Blueprint('movie', __name__)


#just for updation purposees dont use this route
# @movies_bp.route('/update_movie_ids', methods=['GET'])
# def update_movie_ids():
#     try:
#         movies = db.movies.find()
#         for movie in movies:
#             movie_id = uuid.uuid4().hex
#             db.movies.update_one({'_id': movie['_id']}, {'$set': {'movie_id': movie_id}})
#         return jsonify({'message': 'Movie IDs updated successfully'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500





# return all the movies of a particular category


@movies_bp.route('/all/movies/<category>', methods=['GET'])
def get_all_movies(category):
    print(category)
    try:
        if category in ['Bollywood', 'Hollywood']:
            movies = db.movies.find({'Category': category})
            movies_list = list(movies)
            return json.loads(json_util.dumps(movies_list))
        else:
            raise ValueError('Invalid category')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# return 10 or n movies  of a particular category


@movies_bp.route('/movies/<category>', methods=['GET'])
def get_movies(category):
    print(category)
    try:
        if category in ['Bollywood', 'Hollywood']:
            movies = db.movies.find({'Category': category}).limit(1)
            movies_list = list(movies)
            return json.loads(json_util.dumps(movies_list))
        else:
            raise ValueError('Invalid category')
    except Exception as e:
        return jsonify({'error': str(e)}), 400
