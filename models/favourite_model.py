from backend import db


class Favourite:
    collection = db.get_collection('favourites')

    def __init__(self, movie_id, user_id):
        self.movie_id = movie_id
        self.user_id = user_id

    def save(self):
        data = {'movie_id': self.movie_id,
                'user_id': self.user_id}
        result = self.collection.insert_one(data)
        return result.inserted_id
