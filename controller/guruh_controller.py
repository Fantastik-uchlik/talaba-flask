from flask import Blueprint, render_template, request, redirect, url_for

from model.guruh import Guruh
from service.guruh_service import GuruhService
from service.yunalish_service import YunalishService

gs = GuruhService()
ys = YunalishService()

guruh_url = Blueprint("guruh", __name__, template_folder='../templates')


@guruh_url.route("/guruh", methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def index():
    if request.method == 'GET':
        return royxat()
    elif request.method == 'POST':
        return qoshish(request.form)
    elif request.method == 'DELETE':
        return ochirish(request.args.get('id'))


@guruh_url.route("/guruh/ochirish")
def delete():
    return ochirish(request.args.get('id'))


def royxat():
    guruhlar = gs.getAll()
    yunalishlar = ys.getAll()
    return render_template("guruh.html", guruhlar=guruhlar, yunalishlar=yunalishlar)


def qoshish(g):
    guruh = Guruh(g['nom'], g['yunalish_id'], g['yil'], g['til'])
    gs.create(guruh)
    return royxat()


def ochirish(id):
    if id:
        gs.deleteById(id)
    return redirect("/guruh")
