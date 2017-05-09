from flask import render_template

# local imports
from . import main
from .utils import (
        date_converter,
        date_analyzer,
        unixts_converter
    )

@main.route("/")
def homepage():
    return render_template("index.html")


@main.route("/<date_str>")
def timestamp(date_str):
    date_format = date_analyzer(date_str)
    nl_date_str = "none"

    if date_format == "unix_timestamp":
        # convert it to natural language
        ts = int(date_str)
        nl_date_str = unixts_converter(ts)
        return nl_date_str

    nl_date_str = date_converter(date_str)

    return nl_date_str
