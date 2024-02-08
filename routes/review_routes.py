from flask import Blueprint, request, jsonify
from backend.models.rate_review_model import Review
from flask import Blueprint
from backend import db


review_bp = Blueprint('review', __name__)


@review_bp.route('/add_review', methods=['POST'])
def add_review():
    try:
        data = request.json
        movie_id = data.get('movie_id')
        user_id = data.get('user_id')
        userName = data.get('userName')
        acting = data.get('acting')
        music = data.get('music')
        storyline = data.get('storyline')
        cinematography = data.get('cinematography')
        direction = data.get('direction')
        review_title = data.get('review_title')
        review = data.get('review')
        isSpoiler = data.get('isSpoiler')

        if None in [acting, music, storyline, cinematography, direction, review_title, review, isSpoiler]:
            return jsonify({'error': 'All fields are required'}), 400

        # Create a new review object
        new_review = Review(acting=acting, music=music, storyline=storyline, cinematography=cinematography,
                            direction=direction, review_title=review_title, review=review, isSpoiler=isSpoiler, movie_id=movie_id, userName=userName, user_id=user_id)

        # Save the review to the database
        review_id = new_review.save()

        return jsonify({'review_id': review_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@review_bp.route('/reviews/<movie_id>', methods=['GET'])
def get_reviews_for_movie(movie_id):
    try:
        # get all the reviews by excluding the _id field
        reviews = db.reviews.find({'movie_id': movie_id}, {'_id': 0})
        reviews_list = list(reviews)
        print(reviews_list)
        return jsonify({'reviews': reviews_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
