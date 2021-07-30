from config.data_source import db


class Guruh(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100))
    yunalish_id = db.Column(db.Integer, db.ForeignKey('yunalish.id'), nullable=False)
    yunalish = db.relationship('Yunalish', backref=db.backref('guruhlar', lazy=True))
    yil = db.Column(db.Integer)
    til = db.Column(db.String(20))

    def __init__(self, nom, yunalish_id, yil, til):
        self.nom = nom
        self.yunalish_id = yunalish_id
        self.yil = yil
        self.til = til

