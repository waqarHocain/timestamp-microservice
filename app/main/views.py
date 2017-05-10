from flask import ( 
        jsonify,
        redirect,
        render_template,
        request,
        url_for
    )

# local imports
from . import main
from .utils import (
        date_converter,
        date_to_timestamp,
        date_analyzer,
        unixts_converter
    )

@main.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        d = request.form["date_input"]
        return redirect(url_for(".timestamp", date_str=d))

    return render_template("index.html")


@main.route("/<date_str>")
def timestamp(date_str):
    date_format = date_analyzer(date_str)

    timestamp = None
    nl_date_str = None

    if date_format == "unix_timestamp":
        # convert it to natural language
        ts = int(date_str)
        nl_date_str = unixts_converter(ts)
        timestamp = ts
        return jsonify(unix=timestamp, natural=nl_date_str)

    nl_date_str = date_converter(date_str)
    timestamp = date_to_timestamp(date_str)

    return jsonify(unix=timestamp, natural=nl_date_str)
