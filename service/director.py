from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        all_directors = self.dao.get_all()
        return all_directors

    def create(self, data):
        return self.dao.create(data)

    def delete(self, gid):
        self.dao.delete(gid)
