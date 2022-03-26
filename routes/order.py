from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderCreateForm import OrderCreateForm
from utils.db import db
from models.order import Order
from datetime import date

orders = Blueprint("orders", __name__, url_prefix="/orders")


@orders.route("/")
@login_required
def home():
    orderList = Order.query.all()
    return render_template("orders/home.html", items=orderList, user=current_user)


@orders.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderCreateForm()
    if form.validate_on_submit():
        buyer = form.buyer.data
        provider = form.provider.data
        newOrder = Order(buyer, provider)
        db.session.add(newOrder)
        db.session.commit()
        return redirect(url_for("orders.home"))
    return render_template("orders/create.html", form=form)

@orders.route("/finalize/<int:id>")
@login_required
def finalize(id):
    currentOrder = Order.query.get(id)
    currentDate = date.today().isoformat()
    currentOrder.date = currentDate
    db.session.add(currentOrder)
    db.session.commit()
    return redirect(url_for("orders.home"))

@orders.route("/delete/<int:buyer>/<int:id>")
@login_required
def delete(buyer, id):
    if current_order.id == id:
        currentorder = Task.query.filter_by(id=id).first()
        db.session.delete(currentorder)
        db.session.commit()
    return redirect(url_for("orders.home", id=id))