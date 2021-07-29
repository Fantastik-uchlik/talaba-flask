from config.data_source import db
from model.guruh import Guruh


class GuruhRepo():
    def findById(self, id):
        return db.session.query(Guruh).filter(Guruh.id == id).first()
    def findAll(self):
        return db.session.query(Guruh).all()

    def create(self, guruh):
        db.session.add(guruh)
        db.session.commit()
        return True

    def deleteById(self, id):
        m = self.findById(id)
        db.session.delete(m)
        db.session.commit()
        return True
