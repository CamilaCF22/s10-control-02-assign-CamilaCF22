from utils.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.String(50), nullable=False)
    provider = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=True)
    totalSale = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    tax = db.Column(db.Integer, nullable=False)

    def __init__(self, buyer, provider, date, date=None, totalSale=0, discount=20, tax=10 ) -> None:
        self.buyer = buyer
        self.provider = provider
        self.date = date
        self.totalSale = totalSale
        self.discount = discount
        self.tax = tax

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.buyer}, '{self.provider}', '{self.date}', '{self.totalSale}', '{self.discount}','{self.tax}')"