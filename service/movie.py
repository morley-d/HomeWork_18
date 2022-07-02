# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from sqlalchemy.exc import NoResultFound

from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all_with_condition(self, req_data):
        all_movies = self.dao.get_all()
        if 'director_id' in req_data:
            did = req_data.get('director_id')
            all_movies = self.dao.filter_movie_by_director(all_movies, did)
        if 'genre_id' in req_data:
            gid = req_data.get('genre_id')
            all_movies = self.dao.filter_movie_by_genre(all_movies, gid)
        if 'year' in req_data:
            year = req_data.get('year')
            all_movies = self.dao.filter_movie_by_year(all_movies, year)
        return all_movies

    def create(self, movie_data):
        return self.dao.create(movie_data)

    def update(self, mid, movie_data):
        movie = self.dao.get_one_for_update_or_del(mid)
        if not movie:
            raise NoResultFound
        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")
        self.dao.update(movie)

    def update_partial(self, mid, movie_data):
        movie = self.dao.get_one_for_update_or_del(mid)
        if not movie:
            raise NoResultFound
        if "title" in movie_data:
            movie.title = movie_data.get("title")
        if "description" in movie_data:
            movie.description = movie_data.get("description")
        if "trailer" in movie_data:
            movie.trailer = movie_data.get("trailer")
        if "year" in movie_data:
            movie.year = movie_data.get("year")
        if "rating" in movie_data:
            movie.rating = movie_data.get("rating")
        if "genre_id" in movie_data:
            movie.genre_id = movie_data.get("genre_id")
        if "director_id" in movie_data:
            movie.director_id = movie_data.get("director_id")
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
