from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()

# Da Plan
# take hwat you have now, then...
# populate w/ seed database
# build out server, view functions, html, jinja, login, etc
# check rubric for requirements and calc
# this should put you into a graduating threshold, then you can add hideout stuff for Wednesday
# hideout stuff comes later

class User_Items(db.Model):
    
    __tablename__ = 'user_items'
    
    user_items_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    quantity = db.Column(db.Integer, nullable=False, default=0)

class User(db.Model):

    # rename this to plural
    # user is reserved keyword in postgres

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)

    # first arg searches for a foreign key in designated model then connects them
    stash = db.relationship('User_Items', lazy=False, backref='user')

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} user_items={self.user_items}>"

class Items(db.Model):
    
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), unique=True, nullable=False)

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