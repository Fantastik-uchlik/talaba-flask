from config.data_source import db
from model.yunalish import Yunalish


class YunalishRepo():
    def findById(self, id):
        return db.session.query(Yunalish).filter(Yunalish.id == id).first()
    def findAll(self):
        return db.session.query(Yunalish).all()

    def create(self, yunalish):
        db.session.add(yunalish)
        db.session.commit()
        return True

    def deleteById(self, id):
        m = self.findById(id)
        db.session.delete(m)
        db.session.commit()
        return True

    def update(self, yunalish):
        y = self.findById(yunalish.id)
        y.nom = yunalish.nom
        y.kod = yunalish.kod
        y.izoh = yunalish.izoh
        db.session.commit()
        return True
