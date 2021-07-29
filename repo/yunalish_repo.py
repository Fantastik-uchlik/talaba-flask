from config.data_source import db
from model.yunalish import Yunalish


class YunalishRepo():
    def findAll(self):
        return db.session.query(Yunalish).all()