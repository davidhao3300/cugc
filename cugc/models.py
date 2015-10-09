from cugc import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String, unique=True)
    pic_url = db.Column(db.String)

    def __init__(self, name, url, pic_url):
        self.name = name
        self.url = url
        self.pic_url = pic_url

    def __repr__(self):
        return '<Game %r>' % self.name
