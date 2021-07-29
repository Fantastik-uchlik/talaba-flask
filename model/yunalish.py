from config.data_source import db


class Yunalish(db.Model):
    id = db.Column("uuid",db.Integer, primary_key=True, autoincrement=True, as_uuid=True)
    nom = db.Column(db.String(100))
    kod = db.Column(db.String(15))
    izoh = db.Column(db.String(200))

    def __init__(self, nom, kod, izoh):
        self.nom = nom
        self.kod = kod
        self.izoh = izoh

