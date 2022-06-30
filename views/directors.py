from flask_restx import Resource, Namespace

director_ns = Namespace('directors')

"""Роуты для режисеров"""


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = Director.query
        return movies_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@director_ns.route('/<int:dir_id>')
class DirectorView(Resource):
    def put(self, dir_id: int):
        dir_update = db.session.query(Director).get(dir_id)
        if not dir_update:
            return "Нет такого режиссера", 404
        req_json = request.json
        dir_update.name = req_json['name']
        db.session.add(dir_update)
        db.session.commit()
        return "", 201

    def delete(self, dir_id: int):
        dir = db.session.query(Director).get(dir_id)
        db.session.delete(dir)
        db.session.commit()
        return "", 204