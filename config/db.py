from flask_sqlalchemy import SQLAlchemy
# TODO main.py dagi baza nastroykalirini shu yerga ko'chirish kerak
BAZA = 'sqlite:///talaba.db'
SECRET_KEY = "xxxq122"
db = SQLAlchemy()