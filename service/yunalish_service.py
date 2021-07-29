from repo.yunalish_repo import YunalishRepo


class YunalishService():
    yr = YunalishRepo()
    def getAll(self):
        return self.yr.findAll()

    def create(self, yunalish):
        return self.yr.create(yunalish)

    def deleteById(self, id):
        return self.yr.deleteById(id)
