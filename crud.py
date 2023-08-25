from model import db, User, Items, User_Items, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)