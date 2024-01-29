from flask import Blueprint, request, jsonify
from backend.models.favourite_model import Favourite
from flask import Blueprint
from backend import db
from bson import json_util
import json


favourite_bp = Blueprint('favourite', __name__)

# fetching favourite for a particular user


@favourite_bp.route('/get/favourite/<user_id>', methods=['GET'])
def get_user_favorites(user_id):
    try:
        print(user_id)
        user_favorites = db.user_favorites.find({'user_id': user_id})
        movie_ids = [favorite['movie_id'] for favorite in user_favorites]
        movies = db.movies.find({'_id': {'$in': movie_ids}})
        return json.loads(json_util.dumps(movies))
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@favourite_bp.route('/add/favourite', methods=['POST'])
def add_favourite():
    try:
        data = request.json
        movie_id = data.get('movie_id')
        user_id = data.get('user_id')

        _ = Favourite(movie_id, user_id).save()
        return jsonify({'status': True}), 201

    except Exception as err:
        print(err)
        return jsonify({'error': 'Internal Server Error'}), 500
