
from flask import Blueprint, render_template, request, redirect, url_for

from model.talaba import Talaba
from service.talaba_service import TalabaService

ts = TalabaService()
talaba_url = Blueprint("talaba", __name__, template_folder='../templates')



@talaba_url.route("/talaba", methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def index():
    if request.method == 'GET':
        tahrirlashId = request.args.get('tahrirlash')
        if tahrirlashId:
            y=ts.getById(tahrirlashId)
            if y:
                return ozgartirish(y)
        return royxat()
    elif request.method == 'POST':
        return qoshish(request.form)
    elif request.method == 'DELETE':
        return ochirish(request.args.get('id'))


@talaba_url.route("/talaba/ochirish")
def delete():
    return ochirish(request.args.get('id'))

@talaba_url.route("/talaba/tahrirlash", methods = ['POST'])
def update():
    t = request.form
    talaba = Talaba(t['ism'], t['familiya'], t['telefon'])
    talaba.id = t['id']
    ts.update(talaba)
    return redirect("/talaba")


def royxat():
    talabalar = ts.getAll()
    return render_template("talaba.html", talabalar=talabalar)


def qoshish(t):
    talaba = Talaba(t['ism'], t['familiya'], t['telefon'])
    ts.create(talaba)
    return royxat()


def ochirish(id):
    if id:
        ts.deleteById(id)
    return redirect("/talaba")

def ozgartirish(t):
    talabalar = ts.getAll()
    return render_template("talaba.html", talaba = t, talabalar = talabalar)

