from flask import Flask


from config.db import BAZA, SECRET_KEY, db
from controller.YunalishController import YunalishController

app = Flask(__name__)

# Bazaga bog'lash
app.config['SQLALCHEMY_DATABASE_URI'] = BAZA
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)

YunalishController(app)

if __name__ == "__main__":
    app.run(debug=True)