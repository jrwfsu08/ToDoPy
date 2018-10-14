from flask import Flask, request
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'PyLinks'
db = MongoAlchemy(app)


class MyLinks(db.Document):
    owner = db.StringField()
    long = db.StringField()
    short = db.StringField()


@app.route('/link/add')
def addLinkToMyLinks():
    if request.args.get('owner', '') == '' or request.args.get('long', '') == '' \
            or request.args.get('short', '') == '':
        return "Error Request Parms are not filled out"

    link = MyLinks(owner=request.args.get('owner', '1'), long=request.args.get('long', '2'),
                   short=request.args.get('short', '3'))
    link.save()
    return 'Saved Link'

#should only be in test
@app.route('/link/removeall')
def removeAllLinks():
    docs = MyLinks.query.all()
    for i in range(0, len(docs)):
        docs[i].remove()
    return 'Removed All'

if __name__ == '__main__':
    app.run()