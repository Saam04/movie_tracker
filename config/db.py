from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ✅ Correct Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:8080@localhost/movie_tracker_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)
