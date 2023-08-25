import os
import model
import server
from model import db, User, Items, User_Items

os.system('dropdb EFT_Helper')
os.system('createdb EFT_Helper')

model.connect_to_db(server.app)

# seeds db with 5 users, 5 items, and 5 user stashes containing different items of varying quantities

with server.app.app_context():

    model.db.create_all()

    # 5 users

    jared = User(user_name='jared', email='ratbastard@bnp.gov', password='jaredpeepoweird')
    jason = User(user_name='jason', email='watching@paint.dry', password='fugitman')
    javi = User(user_name='javi', email='resident@word.sayer', password='smdftb')
    randy = User(user_name='randy', email='nia@simp.gg', password='iLUHHsao')
    ben = User(user_name='ben', email='NA@omega.lul', password='korea#1')

    # Items ---------------------------------------------------------------------------------------

    # Hardware

    analog_thermometer = Items(item_name='Analog Thermometer', item_category='Hardware', req_quantity=2)
    a_pack_of_nails = Items(item_name='A Pack of Nails', item_category='Hardware', req_quantity=4)
    bolts = Items(item_name='Bolts', item_category='Hardware', req_quantity=18)
    corrugated_hose = Items(item_name='Corrugated Hose', item_category='Hardware', req_quantity=26)
    duct_tape = Items(item_name='Duct Tape', item_category='Hardware', req_quantity=6)
    electric_drill = Items(item_name='Electric Drill', item_category='Hardware', req_quantity=6)
    electric_motor = Items(item_name='Electric Motor', item_category='Hardware', req_quantity=12)
    heat_exchange_alkali = Items(item_name='Heat-exchange Alkali', item_category='Hardware', req_quantity=2)
    leatherman_multitool = Items(item_name='Leatherman Multitool', item_category='Hardware', req_quantity=1)
    light_bulb = Items(item_name='Light Bulb', item_category='Hardware', req_quantity=14)
    pressure_gauge = Items(item_name='Pressure Gauge', item_category='Hardware', req_quantity=8)
    radiator_helix = Items(item_name='Radiator Helix', item_category='Hardware', req_quantity=8)
    screw_nut = Items(item_name='Screw Nut', item_category='Hardware', req_quantity=12)
    a_pack_of_screws = Items(item_name='A Pack of Screws', item_category='Hardware', req_quantity=20)
    toolset = Items(item_name='Toolset', item_category='Hardware', req_quantity=6)
    silicone_tube = Items(item_name='Silicone Tube', item_category='Hardware', req_quantity=14)
    wrench = Items(item_name='Wrench', item_category='Hardware', req_quantity=4)
    elite_pliers = Items(item_name='Elite Pliers', item_category='Hardware', req_quantity=4)
    fireklean_gun_lube = Items(item_name='FireKlean Gun Lube', item_category='Hardware', req_quantity=1)
    spark_plug = Items(item_name='Spark Plug', item_category='Hardware', req_quantity=5)
    xenomorph_sealing_foam = Items(item_name='Xenomorph Sealing Foam', item_category='Hardware', req_quantity=3)
    handdrill = Items(item_name='Handdrill', item_category='Hardware', req_quantity=1)
    wd_40_100ml = Items(item_name='WD-40 100ml', item_category='Hardware', req_quantity=4)
    shustrilo_sealing_foam = Items(item_name='Shustrilo Sealing Foam', item_category='Hardware', req_quantity=5)

    # Electronics
    cpu_fan = Items(item_name='CPU Fan', item_category='Electronics', req_quantity=50)
    capacitors = Items(item_name='Capacitors', item_category='Electronics', req_quantity=12)
    car_battery = Items(item_name='Car Battery', item_category='Electronics', req_quantity=5)
    damaged_hard_drive = Items(item_name='Damaged Hard Drive', item_category='Electronics', req_quantity=4)
    phase_control_relay = Items(item_name='Phase Control Relay', item_category='Electronics', req_quantity=16)
    power_supply_unit = Items(item_name='Power Supply Unit', item_category='Electronics', req_quantity=15)
    powercord = Items(item_name='Powercord', item_category='Electronics', req_quantity=13)
    printed_circuit_board = Items(item_name='Printed Circuit Board', item_category='Electronics', req_quantity=10)
    ssd_drive = Items(item_name='SSD Drive', item_category='Electronics', req_quantity=1)
    secure_flash_drive = Items(item_name='Secure Flash Drive', item_category='Electronics', req_quantity=3)
    wires = Items(item_name='Wires', item_category='Electronics', req_quantity=53)
    working_lcd = Items(item_name='Working LCD', item_category='Electronics', req_quantity=2)
    nixxor_lens = Items(item_name='NIXXOR Lens', item_category='Electronics', req_quantity=8)
    military_cofdm = Items(item_name='Military COFDM', item_category='Electronics', req_quantity=2)
    vpx_flash_storage_module = Items(item_name='VPX Flash Storage Module', item_category='Electronics', req_quantity=2)
    gas_analyzer = Items(item_name='Gas Analyzer', item_category='Electronics', req_quantity=3)
    military_cable = Items(item_name='Military Cable', item_category='Electronics', req_quantity=8)
    phased_array_element = Items(item_name='Phased Array Element', item_category='Electronics', req_quantity=2)
    military_power_filter = Items(item_name='Military Power Filter', item_category='Electronics', req_quantity=4)

    # Medical

    medical_bloodset = Items(item_name='Medical Bloodset', item_category='Medical', req_quantity=2)
    saline_solution = Items(item_name='Saline Solution', item_category='Medical', req_quantity=7)
    sodium_bicarbonate = Items(item_name='Sodium Bicarbonate', item_category='Medical', req_quantity=3)
    coffee_majaica = Items(item_name='Coffee Majaica', item_category='Medical', req_quantity=3)
    ledx = Items(item_name='LEDX', item_category='Medical', req_quantity=1)
    opthalmoscope = Items(item_name='Opthalmoscope', item_category='Medical', req_quantity=1)

    # Valuables

    bronze_lion = Items(item_name='Bronze Lion', item_category='Valuables', req_quantity=4)
    folder_with_intelligence = Items(item_name='Folder with Intelligence', item_category='Valuables', req_quantity=4)
    gold_skull_ring = Items(item_name='Gold Skull Ring', item_category='Valuables', req_quantity=6)
    golden_neck_chain = Items(item_name='Golden Neck Chain', item_category='Valuables', req_quantity=8)
    roler = Items(item_name='Roler', item_category='Valuables', req_quantity=4)

    test_users = [        jared,
        jason,
        javi,
        randy,
        ben,]
    
    test_items = [

        # items
        analog_thermometer,
        a_pack_of_nails,
        bolts,
        corrugated_hose,
        electric_drill,
        electric_motor,
        heat_exchange_alkali,
        leatherman_multitool,
        light_bulb,
        pressure_gauge,
        radiator_helix,
        screw_nut,
        a_pack_of_screws,
        toolset,
        silicone_tube,
        wrench,
        elite_pliers,
        fireklean_gun_lube,
        spark_plug,
        xenomorph_sealing_foam,
        handdrill,
        wd_40_100ml,
        shustrilo_sealing_foam,
        cpu_fan,
        capacitors,
        car_battery,
        damaged_hard_drive,
        phase_control_relay,
        power_supply_unit,
        powercord,
        printed_circuit_board,
        ssd_drive,
        secure_flash_drive,
        wires,
        working_lcd,
        nixxor_lens,
        military_cofdm,
        vpx_flash_storage_module,
        gas_analyzer,
        military_cable,
        phased_array_element,
        military_power_filter,
        medical_bloodset,
        saline_solution,
        sodium_bicarbonate,
        coffee_majaica,
        ledx,
        opthalmoscope,
        bronze_lion,
        folder_with_intelligence,
        gold_skull_ring,
        golden_neck_chain,
        roler
    ]

    db.session.add_all(test_users)
    db.session.add_all(test_items)
    
    db.session.commit()

    for item in test_items:
        for user in test_users:
            new_user_item = User_Items(user_id=user.user_id, item_id=item.item_id)
            db.session.add(new_user_item)
    db.session.commit()

    # 5 stashes

    # jared_stash = User_Items(user_id=jared.user_id, item_id=analog_thermometer.item_id, quantity=5)
    # jason_stash = User_Items(user_id=jason.user_id, item_id=a_pack_of_nails.item_id, quantity=2)
    # javi_stash = User_Items(user_id=javi.user_id, item_id=bolts.item_id, quantity=4)
    # randy_stash = User_Items(user_id=randy.user_id, item_id=corrugated_hose.item_id, quantity=10)
    # ben_stash = User_Items(user_id=ben.user_id, item_id=electric_drill.item_id, quantity=8)

    # db.session.add_all([jared_stash, jason_stash, javi_stash, randy_stash, ben_stash])
    # db.session.commit()


