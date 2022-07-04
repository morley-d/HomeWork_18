from flask_restx import Resource, Namespace
from flask import request, make_response
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.dao.model.genre import genres_schema, genre_schema
from app.implemented import genre_service

genre_ns = Namespace('genres')

"""Роуты для жанров"""

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Получение всех жанров"""
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        """Добавление нового жанра"""
        req_json = request.json
        new_genre = genre_service.create(req_json)
        response = make_response("", 201)
        response.headers['location'] = f"/{genre_ns.path}/{new_genre.id}"
        return response

@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    """Получение одного жанра по id"""
    def get(self, genre_id: int):
        one_genre = genre_service.get_one(genre_id)
        if not one_genre:
            return "Такого жанра нет", 404
        return genre_schema.dump(one_genre), 200

    def delete(self, genre_id: int):
        """Удаление жанра по id"""
        try:
            genre_service.delete(genre_id)
        except UnmappedInstanceError:
            return "Такого жанра нет", 404
        return "", 204