from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        all_genres = self.dao.get_all()
        return all_genres

    def create(self, genre_data):
        return self.dao.create(genre_data)

    def delete(self, gid):
        self.dao.delete(gid)
