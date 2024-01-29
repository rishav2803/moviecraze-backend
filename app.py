from backend import flask_app
from backend.routes.user_routes import user_bp
from backend.routes.movies_routes import movies_bp
from backend.routes.favourite_routes import favourite_bp
from flask_cors import CORS


CORS(flask_app)

print("Registering blueprints...")
flask_app.register_blueprint(user_bp)
flask_app.register_blueprint(movies_bp)
flask_app.register_blueprint(favourite_bp)
print("Blueprints registered!")


if __name__ == '__main__':
    print("Starting the app...")
    flask_app.run(debug=True)
