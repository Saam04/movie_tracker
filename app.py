from flask import Flask
from config.db import app, db
from routes.movie_routes import movie_routes

app.register_blueprint(movie_routes)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "Welcome to the Movie Tracker API!"}

if __name__ == "__main__":
    app.run(debug=True)
