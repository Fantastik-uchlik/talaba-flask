from config.data_source import db
from model.talaba import Talaba


class TalabaRepo():
    def findById(self, id):
        return db.session.query(Talaba).filter(Talaba.id == id).first()
    def findAll(self):
        return db.session.query(Talaba).all()

    def create(self, talaba):
        db.session.add(talaba)
        db.session.commit()
        return True

    def deleteById(self, id):
        m = self.findById(id)
        db.session.delete(m)
        db.session.commit()
        return True

    def update(self, talaba):
        t = self.findById(talaba.id)
        t.ism = talaba.ism
        t.familiya = talaba.familiya
        t.telefon = talaba.telefon
        db.session.commit()
        return True