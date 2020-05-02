__version__ = '0.1.0'

from peewee import *
from datetime import timedelta
from datetime import datetime
import requests
import time
from twisted.internet import task, reactor
import sys

#from initialization import get_log_formatter

queues = ['scholars-portal', "scholars-portal-txt", "clavardez"]
start_url = "https://ca.libraryh3lp.com/presence/jid/"
end_url =  "/chat.ca.libraryh3lp.com/text"


db = SqliteDatabase('presence.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})

class Service(Model):
    """Record queue and their Status to
        AVAILABLE,
        UNAVAILABLE, 
    """
    queue = CharField(max_length=30, null=False)
    status = CharField(max_length=30, null=False)
    date = DateTimeField(default=datetime.now, null=False)

    class Meta:
        database = db

    def __repr__(self):
        return "{0}:{1} :\t{2}".format("Queue",Service.name, Service.status)

def create_table():
    Service.create_table()
    #app_log.info("Created Table Service" )

def seed():
    Service.create(queue='scholars-portal-txt', status="available")
    Service.create(queue='scholars-portal', status="available")
    Service.create(queue='clavardez', status="unavailable")

def check_service_and_insert_to_db():
    """Each minutes during Opening Hours
        a script crawl the Main
        queues to know their status
        
        -scholars-portal-txt
        -scholars-portal
        -clavardez
    """
    for queue in queues:
        url = start_url + queue + end_url
        try:
            response = requests.get(url).content
            response = response.decode("utf-8")
            Service(queue=queue, status=response).save()
        except Exception as e:
            # app_log.error("Can't add value in database"+ str(e) )
            pass


if __name__ == '__main__':
    timeout = 60.0
    try:
        Service.delete().execute() 
    except:
        create_table()
        seed()
        all_db()

