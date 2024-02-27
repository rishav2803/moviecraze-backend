from flask import Blueprint, request, jsonify
# from backend.models.user_model import User
from flask import Blueprint
from backend import db
from bson import json_util
import json
import uuid


movies_bp = Blueprint('movie', __name__)


# just for updation purposees dont use this route
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


@movies_bp.route('/search/<search_term>', methods=['GET'])
def search_movies(search_term):
    try:
        movies = db.movies.find({
            'Series_Title': {'$regex': search_term, '$options': 'i'},
            # '$or': [
            #     {'Series_Title': {'$regex': search_term, '$options': 'i'}},
            #     {'Director': {'$regex': search_term, '$options': 'i'}},
            # ]
        })

        movies_list = list(movies)
        print(movies_list)

        response = {
            'movies': json.loads(json_util.dumps(movies_list)),
        }
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@movies_bp.route('/all/movies/<category>/<page>', methods=['GET'])
def get_all_movies(category, page):
    print(category)
    try:
        pageNo = int(page)
        per_page = 50
        skipVal = (pageNo-1) * per_page
        if category in ['Bollywood', 'Hollywood']:
            movies = db.movies.find({'Category': category}).skip(
                skipVal).limit(per_page)
            count = db.movies.count_documents({'Category': category})
            movies_list = list(movies)

            hasMore = (pageNo)*int(per_page) < int(count)

            response = {
                'movies': json.loads(json_util.dumps(movies_list)),
                'hasMore': hasMore,
            }
            return jsonify(response), 201
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
            movies = db.movies.find({'Category': category}).limit(8)
            movies_list = list(movies)
            return json.loads(json_util.dumps(movies_list)), 201
        else:
            raise ValueError('Invalid category')
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@movies_bp.route('/movie/<movie_id>', methods=['GET'])
def get_movie_by_id(movie_id):
    try:
        movie = db.movies.find_one({'movie_id': movie_id})
        if movie:
            return json.loads(json_util.dumps(movie)), 201
        else:
            return jsonify({'message': 'Movie not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
