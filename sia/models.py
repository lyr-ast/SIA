from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(128))


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    sell_price = db.Column(db.Float, nullable=True)
    rent_price = db.Column(db.Float, nullable=True)
    rent_duration = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "category": self.category,
            "sell_price": self.sell_price,
            "rent_price": self.rent_price,
            "rent_duration": self.rent_duration,
            "description": self.description,
            "image_url": self.image_url,
            "user_id": self.user_id,
        }
    

