import os
from flask import Flask, request, jsonify
from backend.models import db, bcrypt
from backend.resume_routes import resume_bp

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../database"))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "users.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize database and bcrypt
db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(resume_bp, url_prefix="/resume")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)