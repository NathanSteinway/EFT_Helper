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

    analog_thermometer = Items(item_name='Analog Thermometer', item_category='Hardware')
    a_pack_of_nails = Items(item_name='A Pack of Nails', item_category='Hardware')
    bolts = Items(item_name='Bolts', item_category='Hardware')
    corrugated_hose = Items(item_name='Corrugated Hose', item_category='Hardware')
    electric_drill = Items(item_name='Electric Drill', item_category='Hardware')
    electric_motor = Items(item_name='Electric Motor', item_category='Hardware')
    heat_exchange_alkali = Items(item_name='Heat-exchange Alkali', item_category='Hardware')
    leatherman_multitool = Items(item_name='Leatherman Multitool', item_category='Hardware')
    light_bulb = Items(item_name='Light Bulb', item_category='Hardware')
    pressure_gauge = Items(item_name='Pressure Gauge', item_category='Hardware')
    radiator_helix = Items(item_name='Radiator Helix', item_category='Hardware')
    screw_nut = Items(item_name='Screw Nut', item_category='Hardware')
    a_pack_of_screws = Items(item_name='A Pack of Screws', item_category='Hardware')
    toolset = Items(item_name='Toolset', item_category='Hardware')
    silicone_tube = Items(item_name='Silicone Tube', item_category='Hardware')
    wrench = Items(item_name='Wrench', item_category='Hardware')
    elite_pliers = Items(item_name='Elite Pliers', item_category='Hardware')
    fireklean_gun_lube = Items(item_name='FireKlean Gun Lube', item_category='Hardware')
    spark_plug = Items(item_name='Spark Plug', item_category='Hardware')
    xenomorph_sealing_foam = Items(item_name='Xenomorph Sealing Foam', item_category='Hardware')
    handdrill = Items(item_name='Handdrill', item_category='Hardware')
    wd_40_100ml = Items(item_name='WD-40 100ml', item_category='Hardware')
    shustrilo_sealing_foam = Items(item_name='Shustrilo Sealing Foam', item_category='Hardware')

    # Electronics
    cpu_fan = Items(item_name='CPU Fan', item_category='Electronics')
    capacitors = Items(item_name='Capacitors', item_category='Electronics')
    car_battery = Items(item_name='Car Battery', item_category='Electronics')
    damaged_hard_drive = Items(item_name='Damaged Hard Drive', item_category='Electronics')
    phase_control_relay = Items(item_name='Phase Control Relay', item_category='Electronics')
    power_supply_unit = Items(item_name='Power Supply Unit', item_category='Electronics')
    powercord = Items(item_name='Powercord', item_category='Electronics')
    printed_circuit_board = Items(item_name='Printed Circuit Board', item_category='Electronics')
    ssd_drive = Items(item_name='SSD Drive', item_category='Electronics')
    secure_flash_drive = Items(item_name='Secure Flash Drive', item_category='Electronics')
    wires = Items(item_name='Wires', item_category='Electronics')
    working_lcd = Items(item_name='Working LCD', item_category='Electronics')
    nixxor_lens = Items(item_name='NIXXOR Lens', item_category='Electronics')
    military_cofdm = Items(item_name='Military COFDM', item_category='Electronics')
    vpx_flash_storage_module = Items(item_name='VPX Flash Storage Module', item_category='Electronics')
    gas_analyzer = Items(item_name='Gas Analyzer', item_category='Electronics')
    military_cable = Items(item_name='Military Cable', item_category='Electronics')
    phased_array_element = Items(item_name='Phased Array Element', item_category='Electronics')
    military_power_filter = Items(item_name='Military Power Filter', item_category='Electronics')

    # Medical

    medical_bloodset = Items(item_name='Medical Bloodset', item_category='Medical')
    saline_solution = Items(item_name='Saline Solution', item_category='Medical')
    sodium_bicarbonate = Items(item_name='Sodium Bicarbonate', item_category='Medical')
    coffee_majaica = Items(item_name='Coffee Majaica', item_category='Medical')
    ledx = Items(item_name='LEDX', item_category='Medical')
    opthalmoscope = Items(item_name='Opthalmoscope', item_category='Medical')

    # Valuables

    bronze_lion = Items(item_name='Bronze Lion', item_category='Valuables')
    folder_with_intelligence = Items(item_name='Folder with Intelligence', item_category='Valuables')
    gold_skull_ring = Items(item_name='Gold Skull Ring', item_category='Valuables')
    golden_neck_chain = Items(item_name='Golden Neck Chain', item_category='Valuables')
    roler = Items(item_name='Roler', item_category='Valuables')

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


    ])
    
    db.session.commit()

    # 5 stashes

    jared_stash = User_Items(user_id=jared.user_id, item_id=analog_thermometer.item_id, quantity=5)
    jason_stash = User_Items(user_id=jason.user_id, item_id=a_pack_of_nails.item_id, quantity=2)
    javi_stash = User_Items(user_id=javi.user_id, item_id=bolts.item_id, quantity=4)
    randy_stash = User_Items(user_id=randy.user_id, item_id=corrugated_hose.item_id, quantity=10)
    ben_stash = User_Items(user_id=ben.user_id, item_id=electric_drill.item_id, quantity=8)

    db.session.add_all([jared_stash, jason_stash, javi_stash, randy_stash, ben_stash])
    db.session.commit()


