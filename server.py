from flask import Flask, render_template, request, session, flash, redirect
from model import connect_to_db, db, User, Items, User_Items
from jinja2 import StrictUndefined
import os
import crud

app = Flask(__name__)

app.secret_key = os.environ["POSTGRES_URI"]
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/hideout")
def hideout():

    hardware = Items.query.filter_by(item_category='Hardware')
    electronics = Items.query.filter_by(item_category='Electronics')
    medical = Items.query.filter_by(item_category='Medical')
    valuables = Items.query.filter_by(item_category='Valuables')

    return render_template("hideout.html", 
        hardware=hardware,
        electronics=electronics,
        medical=medical,
        valuables=valuables,
    )

@app.route("/quests")
def quests():
    return render_template("quests.html")

@app.route("/ammo")
def ammo():
    return render_template("ammo.html")

@app.route("/armor")
def armor():
    return render_template("armor.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)