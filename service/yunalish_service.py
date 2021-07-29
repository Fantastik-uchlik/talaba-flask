from repo.yunalish_repo import YunalishRepo


class YunalishService():
    yr = YunalishRepo()
    def getAll(self):
        return self.yr.findAll()
