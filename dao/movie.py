from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, movie_data):
        ent = Movie(**movie_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, movie_id):
        movie = self.get_one(movie_id)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_data):
        movie = self.get_one(movie_data.get("id"))
        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")

        self.session.add(movie)
        self.session.commit()
