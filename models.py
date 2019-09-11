from extensions import db

class Houses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sell_price = db.Column(db.Integer)
    list_price = db.Column(db.Integer)
    living_size = db.Column(db.Integer)
    rooms_num = db.Column(db.Integer)
    beds_num = db.Column(db.Integer)
    baths_num = db.Column(db.Integer)
    age = db.Column(db.Integer)
    acres = db.Column(db.Float)
    taxes = db.Column(db.Integer)