from flask import request
from flask_restx import Resource, Namespace
from sqlalchemy.orm.exc import UnmappedInstanceError

from implemented import director_service
from dao.model.director import directors_schema, director_schema

director_ns = Namespace('directors')


"""Роуты для режисеров"""

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:dir_id>')
class DirectorView(Resource):
    def get(self, dir_id: int):
        one_dir = director_service.get_one(dir_id)
        if not one_dir:
            return "Такого режиссера нет", 404
        return director_schema.dump(one_dir), 200

    def delete(self, dir_id: int):
        try:
            director_service.delete(dir_id)
        except UnmappedInstanceError:
            return "Такого режиссера нет", 404
        return "", 204