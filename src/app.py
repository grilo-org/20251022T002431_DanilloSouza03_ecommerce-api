import os
from flask import Flask
from flask_cors import CORS
from src.models.models import db, login_manager, User
from src.controllers.controllers import api_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

CORS(app)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(api_bp)

@app.route('/')
def saudar():
    return "Oi, bem vindo(a) a API Ecommerce!"

with app.app_context():
    db_path = os.path.join(app.instance_path, "ecommerce.db")
    if not os.path.exists(db_path):
        print(db_path)
        print("Creating database...")
        db.create_all()
        print("Database created successfully!")
    else:
        print("Database already exists.")

if __name__ == "__main__":
    app.run(debug=True)