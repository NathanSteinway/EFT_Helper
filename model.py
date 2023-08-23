from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()

class User_Items(db.Model):
    
    __tablename__ = 'user_items'
    
    user_items_id = db.Column(db.Integer, primary_key=True)
    # db.ForeignKey preps db.relationship() for connecting columns between tables
        # User is made
        # Connection is made
            # db.relationship attribute refers to table w/ foreign keys
            # db.relationship connects relevant foreign keys to the designated location
            # db.relationship backref lets User_Items refer to Items to retrieve data
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    quantity = db.Column(db.Integer, nullable=False, default=0)

class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)

    # stash attribute in User class refers to User_Items class for foreign key
    # backref references this instance of this class to help shorten queries

    # example...
    # jared.stash[0].quantity
        # grab jared class obj
        # accesses stash
        # [0] grabs the first item in the list, in this case Bolts
        # since stash[0] is referencing User_Items to return a list of class objects stored in User_Items (Bolts, Nuts, etc), part of that information will be quantity column
        # drill into User_Items class and return the quantity of the quiried item, which is found using the Items class relationship below

    stash = db.relationship('User_Items', lazy=False, backref='user')

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} user_items={self.user_items}>"

class Items(db.Model):
    
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), unique=True, nullable=False)
    item_category = db.Column(db.String(50), nullable=False)

    # stash attribute in User class refers to User_Items class for foreign key
    # backref references this instance of this class to help shorten queries

    # example...
        # jared=User.query.first()
        # jared.stash[0].item.item_name
            # grab jared, access his stash using stash attribute in User class
            # grab the item @ [0]
            # backref in Items, named item, allows the User_Items object to refer to the Items object
            # retrieve the desired attribute
            # User.User_Items.Items(backref).attribute

    stash = db.relationship('User_Items', lazy=False, backref='item')

    def __repr__(self):
        return f"<Items item_name={self.item_name}"

def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("It's ALIIIIVE")

if __name__ == "__main__":
    from server import app

    connect_to_db(app, echo=False)