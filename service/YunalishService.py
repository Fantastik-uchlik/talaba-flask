from repo.YunalishRepo import YunalishRepo


class YunalishService():
    yr = YunalishRepo()

    def getAll(self):
        return self.yr.findAlL()