from flask import render_template, Blueprint




public_url = Blueprint("",__name__, template_folder='templates')


@public_url.route("/")
def index():
    return render_template("index.html")