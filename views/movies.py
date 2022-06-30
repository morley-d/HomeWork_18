# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


"""Роуты для фильмов"""

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # all_movies = Movie.query
        all_movies = db.session.query(Movie.id, Movie.title, Movie.description, Movie.rating,
                                     Movie.trailer, Genre.name.label('genre'),
                                     Director.name.label('director')).join(Genre).join(Director)
        if 'director_id' in request.args:
            did = request.args.get('director_id')
            all_movies = all_movies.filter(Movie.director_id == did)
        if 'genre_id' in request.args:
            gid = request.args.get('genre_id')
            all_movies = all_movies.filter(Movie.genre_id == gid)
        if 'page' in request.args:
            num_page = int(request.args.get('page'))
            all_movies = all_movies.limit(MOVIE_PER_PAGE).offset((num_page - 1) * MOVIE_PER_PAGE)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        # one_movie = Movie.query.get(mid)
        one_movie = db.session.query(Movie.id, Movie.title, Movie.description, Movie.rating,
                                     Movie.trailer, Genre.name.label('genre'),
                                     Director.name.label('director')).join(Genre).join(Director).filter(
                                     Movie.id == mid).one()
        if not one_movie:
            return "Нет такого фильма", 404
        return movie_schema.dump(one_movie), 200

    def patch(self, mid: int):
        # one_movie = Movie.query.get(mid)
        one_movie = db.session.query(Movie).get(mid)
        if not one_movie:
            return "Нет такого фильма", 404
        req_json = request.json
        if 'title' in req_json:
            one_movie.title = req_json['title']
        elif 'description' in req_json:
            one_movie.description = req_json['description']
        elif 'trailer' in req_json:
            one_movie.trailer = req_json['trailer']
        elif 'year' in req_json:
            one_movie.year = req_json['year']
        elif 'rating' in req_json:
            one_movie.rating = req_json['rating']
        elif 'genre_id' in req_json:
            one_movie.genre_id = req_json['genre_id']
        elif 'director_id' in req_json:
            one_movie.director_id = req_json['director_id']
        db.session.add(one_movie)
        db.session.commit()
        return "", 201

    def put(self, mid: int):
        one_movie = db.session.query(Movie).get(mid)
        if not one_movie:
            return "Нет такого фильма", 404
        req_json = request.json
        one_movie.title = req_json['title']
        one_movie.description = req_json['description']
        one_movie.trailer = req_json['trailer']
        one_movie.year = req_json['year']
        one_movie.rating = req_json['rating']
        one_movie.genre_id = req_json['genre_id']
        one_movie.director_id = req_json['director_id']
        db.session.add(one_movie)
        db.session.commit()
        return "", 201

    def delete(self, mid: int):
        one_movie = db.session.query(Movie).get(mid)
        db.session.delete(one_movie)
        db.session.commit()
        return "", 204
