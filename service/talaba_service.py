import re
from repo.talaba_repo import TalabaRepo


class TalabaService():
    tr = TalabaRepo()
    def getAll(self):
        return self.tr.findAll()

    def create(self, talaba):
        return self.tr.create(talaba)

    def deleteById(self, id):
        return self.tr.deleteById(id)
    def getById(self,tahrirlashId):
        return self.tr.findById(tahrirlashId)
    def update(self, talaba):
        return self.tr.update(talaba)
