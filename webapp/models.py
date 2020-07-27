from webapp import app, db

class Op(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    result = db.Column(db.String(300), nullable=False, unique=False)

    def __init__(self, result):
        self.result = result