from backend import db
from backend.helpers.now import now
from typing import Union
import uuid


class Review:
    collection = db.get_collection('reviews')

    def __init__(self, acting, music,storyline,cinematography,direction,review_title,review,isSpoiler,movie_id,userName,user_id):
        self.review_id = uuid.uuid4().hex
        self.movie_id=movie_id
        self.user_id=user_id
        self.userName=userName
        self.acting = acting
        self.music = music
        self.storyline = storyline
        self.cinematography = cinematography
        self.direction = direction
        self.review_title = review_title
        self.review = review
        self.isSpoiler = isSpoiler
        self.created_at = now()
        self.updated_at = now()


    def calculate_avg_score(self) -> Union[float, None]:
        fields = [self.acting, self.music, self.storyline, self.cinematography, self.direction]
        filled_fields = [field for field in fields if field is not None]
        if filled_fields:
            return sum(filled_fields) / len(filled_fields)
        else:
            return None

    def save(self):
        avg_score = self.calculate_avg_score()
        review_data = {
            'review_id':self.review_id,
            'movie_id':self.movie_id,
            'user_id':self.user_id,
            'userName': self.userName,
            'acting': self.acting,
            'music': self.music,
            'storyline': self.storyline,
            'cinematography': self.cinematography,
            'direction': self.direction,
            'review_title': self.review_title,
            'review': self.review,
            'isSpoiler': self.isSpoiler,
            'avg_score': avg_score,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        print(review_data)
        self.collection.insert_one(review_data)
        return self.review_id

