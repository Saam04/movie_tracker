from config.db import db

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    review = db.Column(db.Text, nullable=True)
    tmdb_id = db.Column(db.Integer, unique=True, nullable=False)


    def __repr__(self):
        return f"<Movie {self.title}>"

#db.create_all()
