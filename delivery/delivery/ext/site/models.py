# -*- encoding: utf-8 -*-

from delivery.ext.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.Unicode, unique=True)
    passwd = db.Column("passwd", db.Unicode)
    admin = db.Column("admin", db.Boolean)


class Address(db.Model):
    __tablename__ = "address"
    id = db.Column("id", db.Integer, primary_key=True)
    zip = db.Column("zip", db.Unicode)
    country = db.Column("country", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", foreign_keys=user_id)


class Store(db.Model):
    __tablename__ = "store"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id")
    )

    user = db.relationship("User", foreign_keys=user_id)
    category = db.relationship("Category", foreign_keys=category_id)


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)


# pedidos
class Order(db.Model):
    __tablename__ = "order"
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    address_id = db.Column(
        "address_id", db.Integer, db.ForeignKey("address.id")
    )
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))

    address = db.relationship("Address", foreign_keys=address_id)
    user = db.relationship("User", foreign_keys=user_id)
    store = db.relationship("Store", foreign_keys=store_id)


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    image = deferred(Column("image", db.LargeBinary))
    price = db.Column("price", db.Numeric)
    available = db.Column("available", db.Boolean)
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))

    store = db.relationship("Store", foreign_keys=store_id)


class OrderItems(db.Model):
    __tablename__ = "order_items"
    id = db.Column("id", db.Integer, primary_key=True)
    amount = db.Column("amount", db.Integer)
    items_id = db.Column("items_id", db.Integer, db.ForeignKey("items.id"))
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    items = db.relationship("Items", foreign_keys=items_id)
    order = db.relationship("Order", foreign_keys=order_id)


class Checkout(db.Model):
    __tablename__ = "checkout"
    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Unicode)
    total = db.Column("total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    order = db.relationship("Order", foreign_keys=order_id)
