from flask import Flask, render_template
from model import connect_to_db, db
import os

app = Flask(__name__)

app.secret_key = os.environ["POSTGRES_URI"]

@app.route("/")
def home():
    return render_template("base.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)