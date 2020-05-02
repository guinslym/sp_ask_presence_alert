__version__ = '0.1.0'

from peewee import *
from datetime import timedelta
from datetime import datetime
import time

#from initialization import get_log_formatter

import random

db = SqliteDatabase('presence.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})

class Queue(Model):
    """Record queue and their Status to
        AVAILABLE,
        UNAVAILABLE, 
    """
    name = CharField(max_length=30, null=False)
    status = CharField(max_length=30, null=False)
    date = DateTimeField(default=datetime.now, null=False)

    class Meta:
        database = db

    def __repr__(self):
        return "{0}:{1} :\t{2}".format("Queue",Queue.name, Queue.status)

def create_table():
    Queue.create_table()
    #app_log.info("Created Table Queue" )

def seed():
    Queue.create(name='scholars-portal-txt', status="available")
    Queue.create(name='scholars-portal', status="available")
    Queue.create(name='clavardez', status="available")

if __name__ == '__main__':
    try:
        Queue.delete().execute() 
    except:
        create_table()
        seed()
        all_db()
