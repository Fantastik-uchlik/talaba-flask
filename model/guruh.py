from config.data_source import db


class Guruh(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100))
    kod = db.Column(db.String(15))
    tili = db.Column(db.String(20))

    def __init__(self, nom, kod, tili):
        self.nom = nom
        self.kod = kod
        self.tili = tili

