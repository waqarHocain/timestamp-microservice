import re
from datetime import datetime

# third party imports
from dateutil import parser


def date_analyzer(_date):
    """Analyze whether given input is in unix timestamp form
    or natural language form (jan 1, 1990)"""
    try:
        d = int(_date)
    except ValueError:
        return "natural_language"

    return "unix_timestamp"


def unixts_converter(unix_ts):
    """Returns a human readable date in following format,
    given unix timestamp as an argument
        "May 8, 2017" 
    """
    dt = datetime.utcfromtimestamp(unix_ts)
    
    result = dt.strftime("%B %e, %Y")
    result = re.sub(r"\s+", " ", result)

    return result


def date_converter(date_str):
    """Returns a convenient to read str with date in following format,
    given an somewhat not so convenient date str
        "August 14, 1947"
    """
    try:
        d = parser.parse(date_str)
    except ValueError:
        d = "none"

    if d == "none":
        return "none"

    # remove extra whitespace
    result = d.strftime("%B %e, %Y")
    result = re.sub(r"\s+", " ", result)
    
    return result
