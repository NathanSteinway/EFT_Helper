from flask import Flask, render_template, redirect, flash, request, jsonify
from model import connect_to_db, db, User, Items, User_Items
from jinja2 import StrictUndefined

from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

import os
import crud
import requests

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

        return redirect("/hideout")
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        all_items = Items.query.all()
        new_user = User(user_name=form.username.data, email=form.email.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        for item in all_items:
            new_user_item = User_Items(user_id=new_user.user_id, item_id=item.item_id)
            db.session.add(new_user_item)
        db.session.commit()

        return redirect('/hideout')
    
    return render_template('register.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route("/increment/<user_item_id>")
@login_required
def increment(user_item_id):

    
    user_item = User_Items.query.get(user_item_id)
    old_quantity = user_item.quantity
    user_item.quantity = old_quantity + 1

    db.session.add(user_item)
    db.session.commit()
    
    return redirect('/hideout')

@app.route("/decrement/<user_item_id>")
@login_required
def decrement(user_item_id):

    
    user_item = User_Items.query.get(user_item_id)
    old_quantity = user_item.quantity
    user_item.quantity = old_quantity - 1

    db.session.add(user_item)
    db.session.commit()
    
    return redirect('/hideout')

@app.route("/hideout")
def hideout():

    if current_user.is_authenticated == False:        
        flash('Log in to view your hideout!')
        return redirect("/login")


    # Logic for TarkovAPI here

    # hardware = Items.query.filter_by(item_category='Hardware')
    # electronics = Items.query.filter_by(item_category='Electronics')
    # medical = Items.query.filter_by(item_category='Medical')
    # valuables = Items.query.filter_by(item_category='Valuables')

    # update quantity of value on specific user item
    # user item being in this for loop below

    hardware = []
    electronics = []
    medical = []
    valuables = []

    for user_item in current_user.stash:
        
        if user_item.item.item_category == 'Hardware':
            hardware.append(user_item)
        elif user_item.item.item_category == 'Electronics':
            electronics.append(user_item)
        elif user_item.item.item_category == 'Medical':
            medical.append(user_item)
        elif user_item.item.item_category == 'Valuables':
            valuables.append(user_item)
    
    def alphabetical(user_item):
        return user_item.item.item_name

    hardware_sorted = sorted(hardware, key=alphabetical)
    electronics_sorted = sorted(electronics, key=alphabetical)
    medical_sorted = sorted(medical, key=alphabetical)
    valuables_sorted = sorted(valuables, key=alphabetical)
    
    return render_template("hideout.html", 
        hardware_sorted=hardware_sorted,
        electronics_sorted=electronics_sorted,
        medical_sorted=medical_sorted,
        valuables_sorted=valuables_sorted,
    )

@app.route("/quests")
def quests():

    def run_query(query):
            headers = {"Content-Type": "application/json"}
            response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

    # Change this to match eft-ammo parameters
    new_query = """
    {
        tasks {
            name
            objectives {
                description
            }
            trader {
                imageLink
            }
        }
    }
    """

    result = run_query(new_query)
    print(result['data']['tasks'])
    return render_template("quests.html", quest_list=result['data']['tasks'])

@app.route("/ammo")
def get_ammo():

    def run_query(query):
        headers = {"Content-Type": "application/json"}
        response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

    # Change this to match eft-ammo parameters
    new_query = """
    {
        ammo {
            item {
                name
                baseImageLink
                    properties {
                        ... on ItemPropertiesAmmo {
                            caliber
                            damage
                            penetrationPower
                            fragmentationChance
                            accuracyModifier
                            initialSpeed
                        }
                    }
            }
        }
    }
    """

    result = run_query(new_query)
    print(result)
    return render_template("ammo.html", ammunition_list=result['data']['ammo'])

@app.route("/armor")
def armor():

    def run_query(query):
        headers = {"Content-Type": "application/json"}
        response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))
        
    armor_query = """
        {
            armorItems: items(type: armor) {
                name
                baseImageLink
                properties {
                    ... on ItemPropertiesArmor {
                        armorType
                        class
                        durability
                        ergoPenalty

                        material {
                            name
                        }

                        repairCost
                        speedPenalty
                        turnPenalty
                        zones
                    }
                }
            }

            rigItems: items(type: rig) {
                name
                baseImageLink
                properties {
                    ... on ItemPropertiesChestRig {
                        armorType
                        class
                        durability
                        ergoPenalty

                        material {
                            name
                        }

                        repairCost
                        speedPenalty
                        turnPenalty
                        zones
                    }
                }
            }
        }
    """

    result = run_query(armor_query)

    # Separates data, preps new list
    armor_list = result['data']['armorItems']
    rig_list = result['data']['rigItems']
    combined_list = []

    # Checks whether or not the properties field is populated
    # If yes, assign item_type w/ value of 'armor'
    # If no, say so!
    for armor in armor_list:
        if armor.get('properties'):
            armor['item_type'] = 'armor'
            combined_list.append(armor)
        else:
            print('Rig Detected')
        
    # Checks the fields contained within properties for null values
    # If yes, set unarmored_rig to True
    # If no, assign item_type w/ value of 'rig'
    for rig in rig_list:

        unarmored_rig = False

        for key, value in rig.get('properties', {}).items():
            if value is None:
                unarmored_rig = True
                break

        if not unarmored_rig:
            rig['item_type'] = 'rig'
            combined_list.append(rig)


    return render_template("armor.html", armor_items=combined_list)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)