import os
from flask import Flask, request, jsonify
from backend.models import db, bcrypt, login_manager
from backend.resume_routes import resume_bp
from flask_jwt_extended import JWTManager
app = Flask(__name__)
from backend import routes

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../database"))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "users.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'

db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

app.register_blueprint(resume_bp, url_prefix="/resume")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)