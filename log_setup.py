#Python STD package
import time
from pytz import timezone
from datetime import datetime
import random
from pprint import pprint as print
import os
import logging
from logging.handlers import RotatingFileHandler
import sys

#Installed packages
import pytz
import requests 

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



if __name__ == '__main__':
    pass