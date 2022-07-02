# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.exc import UnmappedInstanceError

from dao.model.movie import movies_schema, movie_schema
from implemented import movie_service

movie_ns = Namespace('movies')


"""Роуты для фильмов"""

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        req_data = request.args
        all_movies = movie_service.get_all_with_condition(req_data)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        try:
            one_movie = movie_service.get_one(mid)
        except NoResultFound:
            return "Нет такого фильма", 404
        # if not one_movie:
        #     return "Нет такого фильма", 404
        return movie_schema.dump(one_movie), 200

    def patch(self, mid: int):
        req_json = request.json
        try:
            movie_service.update_partial(mid, req_json)
        except NoResultFound:
            return "Нет такого фильма", 404
        return "", 201

    def put(self, mid: int):
        req_json = request.json
        try:
            movie_service.update(mid, req_json)
        except NoResultFound:
            return "Нет такого фильма", 404
        return "", 201

    def delete(self, mid: int):
        try:
            movie_service.delete(mid)
        except UnmappedInstanceError:
            return "Такого фильма нет", 404
        return "", 204
