from flask import Blueprint
from controllers.movie_controller import add_movie, get_all_movies, get_movie_by_id, update_movie, delete_movie

movie_routes = Blueprint("movie_routes", __name__)

movie_routes.route("/movies", methods=["POST"])(add_movie)
movie_routes.route("/movies", methods=["GET"])(get_all_movies)
movie_routes.route("/movies/<int:movie_id>", methods=["GET"])(get_movie_by_id)
movie_routes.route("/movies/<int:movie_id>", methods=["PUT"])(update_movie)
movie_routes.route("/movies/<int:movie_id>", methods=["DELETE"])(delete_movie)
