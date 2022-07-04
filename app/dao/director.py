from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, genre_data):
        ent = Director(**genre_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, did):
        dir = self.get_one(did)
        self.session.delete(dir)
        self.session.commit()
