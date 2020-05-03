__version__ = '0.1.0'

from peewee import *
from datetime import timedelta
from datetime import datetime
import requests
import time
import sys

from twilio.rest import Client
from environs import Env
env = Env()
# Read .env into os.environ
env.read_env()

#loggin system
from log_setup import get_log_formatter
app_log = get_log_formatter()

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

    def __str__(self):
        return "{0}:{1} :\t\t{2}".format("Queue",self.queue, self.status)

    def __repr__(self):
        return "{0}:{1} :\t{2}".format("Queue",self.queue, self.status)

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
            Service.insert(queue=queue, status=response).execute()
        except Exception as e:
            app_log.error("Can't add value in database"+ str(e) )
            pass

def get_presence():
    """Insert the presence status in DB
    Go online and check each Service Presence Status
    and insert it in the DB

    i.e. Does the ASK SMS service is open?
    """
    Service.create_table()
    check_service_and_insert_to_db()
    query = Service.select()
    queues = [service.queue for service in query]
    print(len(queues))
    for service in query:
        print(service)

def send_sms(web, clavardez, sms):
    """Will send an SMS to Scholars Portal - Ask Coordinator

    SECRETS: Require .env file or Environment variables

    Arguments:
        web {int} -- Number of Downtime in minutes
        clavardez {int} -- Number of Downtime in minutes
        sms {int} -- Number of Downtime in minutes
    """
    account_sid = env("ACCOUNT_SID")
    auth_token = env("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Ask Service Downtime\nweb-en:\t{0} min\nweb-fr:\t{1} min\nSMS:\t{2} min\n".format(web, clavardez, sms),
        from_=env("FROM"),
        to=env("TO")
    )

def verify_Ask_service(min_alert_minute):
    """If Ask Service is down equal or more of the
     'min_alert_minute' then send SMS

    Arguments:
        min_alert_minute {[type]} -- [description]
    """
    fr_result = Service.select().where((Service.status=="unavailable") and (Service.queue=="clavardez"))
    sms_result = Service.select().where((Service.status=="unavailable") and (Service.queue=="scholars-portal-txt"))
    if (len(fr_result) >= min_alert_minute) | (len(sms_result) >= min_alert_minute) :
        clavardez = len(Service.select().where((Service.status=="unavailable") and (Service.queue=="clavardez")))
        sms = len(Service.select().where((Service.status=="unavailable") and (Service.queue=="scholars-portal-txt")))
        web = len(Service.select().where((Service.status=="unavailable") and (Service.queue=="scholars-portal")))
        print("Ask Service Downtime\nweb-en:\t{0} min\nweb-fr:\t{1} min\nSMS:\t{2} min\n".format(web, clavardez, sms))
        send_sms(web, clavardez, sms)
        sys.exit()

if __name__ == '__main__':
    min_alert_minute = 3
    Service.delete().execute() 
    counter = 0
    while counter < min_alert_minute:
        get_presence()
        time.sleep(60)
        counter +=1
    
    # After 10 min .. check this
    verify_Ask_service(min_alert_minute)

    breakpoint()


