from flask import Flask
from config.db import app, db
from routes.movie_routes import movie_routes

# Register Blueprints
app.register_blueprint(movie_routes)

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/")
def home():
    return {"message": "Welcome to the Movie Tracker API!"}
