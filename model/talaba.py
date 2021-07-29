from config.data_source import db


class Talaba(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ism = db.Column(db.String(50))
    familiya = db.Column(db.String(50))
    telefon = db.Column(db.String(15))

    def __init__(self, ism, familiya, telefon):
        self.ism = ism
        self.familiya = familiya
        self.telefon = telefon

