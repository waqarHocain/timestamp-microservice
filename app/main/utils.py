from datetime import datetime


def unixts_converter(unix_ts):
    """Returns a human readable date in following format,
    given unix timestamp as an argument
        "May 8, 2017" 
    """
    dt = datetime.utcfromtimestamp(unix_ts)

    return dt.strftime("%B%e, %Y")


def date_analyzer(_date):
    """Analyze whether given input is in unix timestamp form
    or natural language form (jan 1, 1990)"""
    try:
        d = int(_date)
    except ValueError:
        return "natural_language"

    return "unix_timestamp"
