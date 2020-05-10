import os
import datetime

def get_datetime():
    dt = datetime.datetime.now()
    return datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M:%S")
