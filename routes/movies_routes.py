from flask import Blueprint, request, jsonify
# from backend.models.user_model import User
from flask import Blueprint
from backend import db
from bson import json_util
import json


movies_bp = Blueprint('movie', __name__)

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
