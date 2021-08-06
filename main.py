from flask import Flask, request, url_for, render_template
from werkzeug.utils import redirect

from config.data_source import DATABASE_URL, SECRET_KEY, db

from controller.guruh_controller import guruh_url
from controller.talaba_controller import talaba_url
from controller.yunalish_controller import yunalish_url
from public_urls import public_url

app = Flask(__name__)

app.register_blueprint(public_url)
app.register_blueprint(yunalish_url)
app.register_blueprint(guruh_url)
app.register_blueprint(talaba_url)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)
app.app_context().push()
db.create_all()




if __name__ == "__main__":
    app.run(debug=True)
