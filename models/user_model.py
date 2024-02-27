from backend import db
from backend.helpers.now import now
import uuid
import bcrypt


class User:
    collection = db.get_collection('users')

    def __init__(self, userName, email, password):
        self.userName = userName
        self.email = email
        self.password = password
        self.user_id = uuid.uuid4().hex
        self.created_at = now()
        self.updated_at = now()

    def save(self):
        hashed_password = bcrypt.hashpw(
            self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_data = {
            'user_id': self.user_id,
            'userName': self.userName,
            'email': self.email,
            'password': hashed_password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        result = self.collection.insert_one(user_data)
        return self.user_id

    @staticmethod
    # check if particular field already exist or not
    # made this static because we need to be able to access it directly using the class name
    def check_if_exist(fieldName, data):
        existing_user = db.users.find_one({fieldName: data})
        return existing_user is not None

    @staticmethod
    # check the password of the exisiting user
    # made this static because we need to be able to access it directly using the class name
    def check_password(email, password):
        user = db.users.find_one({'email': email})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return True, user
        return False, None
