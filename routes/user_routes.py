from flask import Blueprint, request, jsonify
from backend.models.user_model import User
from flask import Blueprint
from backend import db


user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        userName = data.get('userName')
        email = data.get('email')
        password = data.get('password')
        print(userName,email,password)

        if not userName:
            return jsonify({'error': 'Username is required'}), 400

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        if not password:
            return jsonify({'error': 'Password is required'}), 400

        existing_user_name = User.check_if_exist('userName', userName)

        if existing_user_name:
            return jsonify({'mssg': 'Username already exists', 'status': False}), 400

        existing_email = User.check_if_exist('email', email)
        if existing_email:
            return jsonify({'mssg': 'Email already exists', 'status': False}), 400

        user_id = User(userName, email, password).save()

        return jsonify({'user_id': str(user_id)}), 201

    except Exception as err:
        print(err)
        return jsonify({'error': 'Internal Server Error'}), 500


@user_bp.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user_exist = User.check_if_exist('email', email)

        # check if the user already exist or not
        # check if the user does not exist then send error
        if not user_exist:
            return jsonify({'mssg': 'Incorrect Email or Password', 'status': False}), 400

        is_passd_valid, user = User.check_password(email, password)

        # if the password do not match send an error
        if not is_passd_valid and user is None:
            return jsonify({'mssg': 'Incorrect Password', 'status': False}), 400

        user['_id'] = str(user['_id'])

        return jsonify({'user': user, 'status': True}), 201

    except Exception as err:
        print(err)
        return jsonify({'error': 'Internal Server Error'}), 500
