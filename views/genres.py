from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')

"""Роуты для жанров"""

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = Genre.query
        return movies_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201

@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def put(self, genre_id: int):
        genre_update = db.session.query(Genre).get(genre_id)
        if not genre_update:
            return "Нет такого жанра", 404
        req_json = request.json
        genre_update.name = req_json['name']
        db.session.add(genre_update)
        db.session.commit()
        return "", 201

    def delete(self, genre_id: int):
        genre = db.session.query(Genre).get(genre_id)
        db.session.delete(genre)
        db.session.commit()
        return "", 204