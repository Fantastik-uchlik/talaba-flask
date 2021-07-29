from flask import Blueprint, render_template



talaba_url = Blueprint("talaba", __name__, template_folder='../templates')

@talaba_url.route("/talaba")
def ruyxat():
    return render_template("talaba.html")
