from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'library'
db = MongoAlchemy(app)


class MyLinks(db.Document):
    owner = db.StringField()
    long = db.StringField()
    short = db.StringField()
