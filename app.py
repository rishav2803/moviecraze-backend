from backend import flask_app
from backend.routes.user_routes import user_bp

print("Registering blueprints...")
flask_app.register_blueprint(user_bp)
print("Blueprints registered!")


if __name__ == '__main__':
    print("Starting the app...")
    flask_app.run(debug=True)
