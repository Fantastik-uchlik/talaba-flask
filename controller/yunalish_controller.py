from flask import Blueprint, render_template

from service.yunalish_service import YunalishService

ys = YunalishService()


yunalish_url = Blueprint("yunalish", __name__, template_folder='../templates')

@yunalish_url.route("/yunalish")
def ruyxat():
    yunalishlar = ys.getAll()
    return render_template("yunalish.html", yunalishlar = yunalishlar)


