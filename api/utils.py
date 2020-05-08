from datetime import datetime


def jsonDefault(value):
    if isinstance(value, datetime):
        return dict(year=value.year, month=value.month, day=value.day, hour=value.hour, minute=value.minute)
    else:
        return value.__dict__
