[
![PyPI](https://img.shields.io/pypi/v/ask_schools.svg)
![PyPI](https://img.shields.io/pypi/pyversions/ask_schools.svg)
![PyPI](https://img.shields.io/github/license/guinslym/ask_schools.svg)
](https://pypi.org/project/ask_schools/)
[![TravisCI](https://travis-ci.org/guinslym/ask_schools.svg?branch=master)](https://travis-ci.org/guinslym/ask_schools)
<hr/>


## SP ASK Service SMS Alert script

Script to ping our 3  main LibraryH3lp services (web, clavardez, sms) and if one of the queue is close during standard Ask opening Hours after 15 minutes it will send an SMS or email to Scholars-Portal
<br/>


## Installation


**SP ASK Service SMS Alert** is not a package but a **script** and can run by typing this in the terminal:

```
## using pip 
pip install -r requirements.txt
python sp_ask_service_availability_alert.py

## or using poetry
poetry install 
poetry run python sp_ask_service_availability_alert.py

## if above (poetry) installed; Use make
make run
```
In addition it is useful to execute it from **crontab**
`*/15 * * * * python sp_ask_service_availability_alert.py`

## Requirement
1.  This script requires a TWILIO account credentials to send SMS 
2.  This script requires a .env file 

```text

# .env
ACCOUNT_SID="Twillio account sid"
AUTH_TOKEN="twillio auth token"
FROM="phone number"
TO="phone number"
```

## Screenshots
This is a mockup, it will only send if one of the services has been down for at least 10 minutes
<p float="left">
    <img src="screenshots/result_sms.png" width="400"/>
</p>


## Todo

1.  Add condition to run only on Ask open hours
2.  Replace SMS with email to ASK SP inbox
2.  Add tests
3.  Add Docker

