from flask import render_template


from service.YunalishService import YunalishService


class YunalishController():
    ys = YunalishService()

    def __init__(self, app):
        app.add_url_rule("/", 'yunalish', self.royxat)

    def royxat(self):
        yunalishlar = self.ys.getAll()

        return render_template("yunalish-royxat.html", yunalishlar=yunalishlar)
