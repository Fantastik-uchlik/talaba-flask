from flask import Blueprint, render_template



guruh_url = Blueprint("guruh", __name__, template_folder='../templates')

@guruh_url.route("/guruh")
def ruyxat():
    return render_template("guruh.html")
