import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

# Ensure this function exists
def fetch_movie_details(title):
    url = f"{TMDB_BASE_URL}/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": title}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "results" in data and data["results"]:
        movie = data["results"][0]  # Get the first search result
        return {
            "title": movie["title"],
            "year": int(movie["release_date"].split("-")[0]) if movie.get("release_date") else None,
            "tmdb_id": movie["id"],
            "rating": movie.get("vote_average", 0)
        }
    
    return None  # Return None if no movie is found
