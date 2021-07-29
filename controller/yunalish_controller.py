from flask import Blueprint, render_template, request, redirect, url_for

from model import Yunalish
from service.yunalish_service import YunalishService

ys = YunalishService()

yunalish_url = Blueprint("yunalish", __name__, template_folder='../templates')


@yunalish_url.route("/yunalish", methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def index():
    if request.method == 'GET':
        return royxat()
    elif request.method == 'POST':
        return qoshish(request.form)
    elif request.method == 'DELETE':
        return ochirish(request.args.get('id'))


@yunalish_url.route("/yunalish/ochirish")
def delete():
    return ochirish(request.args.get('id'))


def royxat():
    yunalishlar = ys.getAll()
    return render_template("yunalish.html", yunalishlar=yunalishlar)


def qoshish(y):
    yunalish = Yunalish(y['nom'], y['kod'], y['izoh'])
    ys.create(yunalish)
    return royxat()


def ochirish(id):
    if id:
        ys.deleteById(id)
    return redirect("/yunalish")
