# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie.id, Movie.title, Movie.description, Movie.rating,
                                     Movie.trailer, Genre.name.label('genre'),
                                     Director.name.label('director')).join(Genre).join(Director).filter(
                                     Movie.id == mid).one()

    def get_one_for_update_or_del(self, mid):
        return self.session.query(Movie).get(mid)


    def get_all(self):
        return self.session.query(Movie.id, Movie.title, Movie.description,Movie.year, Movie.rating,
                                      Movie.trailer, Genre.name.label('genre'),
                                      Director.name.label('director')).join(Genre).join(Director)

    def filter_movie_by_director(self, all_movies, did):
        return all_movies.filter(Movie.director_id == did)

    def filter_movie_by_genre(self, all_movies, gid):
        return all_movies.filter(Movie.genre_id == gid)

    def filter_movie_by_year(self, all_movies, year):
        return all_movies.filter(Movie.year == year)

    def create(self, movie_data):
        ent = Movie(**movie_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, movie_id):
        movie = self.get_one_for_update_or_del(movie_id)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
