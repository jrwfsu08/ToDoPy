from flask import Flask, request
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'Links'
db = MongoAlchemy(app)


class MyLinks(db.Document):
    owner = db.StringField()
    long = db.StringField()
    short = db.StringField()


@app.route('/link/add')
def addLinkToMyLinks():
    link = MyLinks(owner=request.args.get('owner', '1'), long=request.args.get('long','2'), short=request.args.get('long','3'))
    link.save()
    return 'Saved Link'