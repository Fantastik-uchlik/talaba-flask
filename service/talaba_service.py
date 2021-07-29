from repo.talaba_repo import TalabaRepo


class TalabaService():
    tr = TalabaRepo()
    def getAll(self):
        return self.tr.findAll()

    def create(self, yunalish):
        return self.tr.create(yunalish)

    def deleteById(self, id):
        return self.tr.deleteById(id)
