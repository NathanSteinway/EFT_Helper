from flask import Flask, render_template, redirect, flash
from model import connect_to_db, db, User, Items, User_Items
from jinja2 import StrictUndefined

from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

import os
import crud

app = Flask(__name__)

app.secret_key = os.environ["POSTGRES_URI"]
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegisterForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Username"})
    
    email = StringField(
        validators=[InputRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Email"})

    password = PasswordField(
        validators=[InputRequired(), Length(min=12, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(min=1, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(
        validators=[InputRequired(), Length(min=12, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(user_name=form.username.data).first()

        login_user(user)

        flash('You are logged in.')

        return redirect("/hideout")
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        all_items = Items.query.all()
        new_user = User(user_name=form.username.data, email=form.email.data, password=form.password.data)
        new_stash = User_Items(user_id=new_user.user_id, item_id=all_items)

        db.session.add(new_user, new_stash)
        db.session.commit()

        return redirect('/hideout')
    
    return render_template('register.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You are logged out.')
    return redirect('/login')

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