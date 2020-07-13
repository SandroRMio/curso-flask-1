# -*- encoding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class TblUser(db.Model):
    __tablename__ = "tbl_user"
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.Unicode)

class TblTodo(db.Model):
    __tablename__ = "tbl_todo"
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.Unicode)
    done = db.Column('done', db.Boolean)
    tbl_user_id = db.Column('tbl_user_id', db.Integer, db.ForeignKey('tbl_user.id'))

    tbl_user = db.relationship('TblUser', foreign_keys=tbl_user_id)

