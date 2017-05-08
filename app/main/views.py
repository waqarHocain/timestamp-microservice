from flask import render_template

# local imports
from . import main


@main.route("/")
def homepage():
    return render_template("index.html")
