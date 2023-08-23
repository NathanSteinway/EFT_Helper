import os
import model
import server
from model import db, User, Items, User_Items

os.system('dropdb EFT_Helper')
os.system('createdb EFT_Helper')

model.connect_to_db(server.app)

with server.app.app_context():

    model.db.create_all()

    jared = User(user_name='jared', email='ratbastard@bnp.gov', password='jaredpeepoweird')
    jason = User(user_name='jason', email='watching@paint.dry', password='fugitman')
    javi = User(user_name='javi', email='resident@word.sayer', password='smdftb')
    randy = User(user_name='randy', email='nia@simp.gg', password='iLUHHsao')
    ben = User(user_name='ben', email='NA@omega.lul', password='korea#1')

    analog_thermometer = Items(item_name='Analog Thermometer')
    a_pack_of_nails = Items(item_name='A Pack of Nails')
    bolts = Items(item_name='Bolts')
    corrugated_hose = Items(item_name='Corrugated Hose')
    electric_drill = Items(item_name='Electric Drill')

    db.session.add_all([
        # users
        jared,
        jason,
        javi,
        randy,
        ben,

        # items
        analog_thermometer,
        a_pack_of_nails,
        bolts,
        corrugated_hose,
        electric_drill
    ])
    
    db.session.commit()

    jared_stash = User_Items(user_id=jared.user_id, item_id=analog_thermometer.item_id, quantity=5)
    jason_stash = User_Items(user_id=jason.user_id, item_id=a_pack_of_nails.item_id, quantity=2)
    javi_stash = User_Items(user_id=javi.user_id, item_id=bolts.item_id, quantity=4)
    randy_stash = User_Items(user_id=randy.user_id, item_id=corrugated_hose.item_id, quantity=10)
    ben_stash = User_Items(user_id=ben.user_id, item_id=electric_drill.item_id, quantity=8)

    db.session.add_all([jared_stash, jason_stash, javi_stash, randy_stash, ben_stash])
    db.session.commit()


