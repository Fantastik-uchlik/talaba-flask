
from model.Yunalish import Yunalish
from config.db import db

class YunalishRepo():

    def findAlL(self):
        return db.session.query(Yunalish).all()