from flask import jsonify, request
from models.movie_model import Movie, db
from utils.tmdb import fetch_movie_details

def add_movie():
    data = request.json
    title = data.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    movie_data = fetch_movie_details(title)
    if not movie_data:
        return jsonify({"error": "Movie not found on TMDb"}), 404

    new_movie = Movie(**movie_data)
    db.session.add(new_movie)
    db.session.commit()

    return jsonify({"message": "Movie added", "movie": movie_data}), 201

def get_all_movies():
    page = request.args.get("page", 1, type=int)  
    per_page = request.args.get("per_page", 10, type=int)  

    movies = Movie.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify(
        {
        "movies": [
            {
                "id": movie.id,
                "title": movie.title,
                "year": movie.year,
                "rating": movie.rating,
                "review": movie.review
            } for movie in movies.items
        ],
        "total_pages": movies.pages,
        "current_page": movies.page
    }
)

def get_movie_by_id(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    return jsonify({
        "id": movie.id,
        "title": movie.title,
        "year": movie.year,
        "rating": movie.rating,
        "review": movie.review
    })

def update_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    data = request.json
    movie.rating = data.get("rating", movie.rating)
    movie.review = data.get("review", movie.review)
    
    db.session.commit()
    return jsonify({"message": "Movie updated"})

def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Movie deleted"})
