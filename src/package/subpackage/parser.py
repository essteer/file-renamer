def date_parser(string):
    """Receives a DateTime string from image metadata.
    Returns a string with colons removed and date and time joined
    with an underscore ('_')."""
    date, time = string.split()

    date = ("").join(date.split(":"))
    time = ("").join(time.split(":"))

    return date + "_" + time
