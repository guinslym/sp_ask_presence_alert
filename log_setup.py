import requests 
import sched, time
import pytz
from pytz import timezone
from datetime import datetime
import random

from pprint import pprint as print
import os

import logging
from logging.handlers import RotatingFileHandler
import sys

import lh3.api
# client = lh3.api.Client()
# client.set_options(version = 'v1')

fmt_date = '%Y-%m-%d'
fmt_hour = '%H:%M:%S'
fmt_hour_round = '%H.%M'
utc = pytz.utc
eastern = timezone('America/Montreal')

def get_log_formatter():
    # https://tutorialedge.net/python/python-logging-best-practices/
    log_formatter = logging.Formatter('%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s')
    logFile = './log.log'
    my_handler = RotatingFileHandler(
        logFile, mode='a', maxBytes=5*1024*1024,
        backupCount=2, encoding=None, delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)
    app_log = logging.getLogger('root')
    app_log.setLevel(logging.INFO)
    app_log.addHandler(my_handler)
    return app_log

def is_hour_between(start, end, now):
    is_between = False

    is_between |= start <= now <= end
    is_between |= end < start and (start <= now or now <= end)

    return is_between

def find_which_weekday():
    day = datetime.today().weekday()
    if day >= 1 and day < 5:
        return [9.5, 22.15]
    elif day == 5:
        return [9.5, 17.15]
    else:
        #weekend
        return [11.5, 1.5]

if __name__ == '__main__':
    #presence 
    #chat_activity_excel try...
    pass