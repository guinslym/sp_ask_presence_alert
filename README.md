[
![PyPI](https://img.shields.io/pypi/v/ask_schools.svg)
![PyPI](https://img.shields.io/pypi/pyversions/ask_schools.svg)
![PyPI](https://img.shields.io/github/license/guinslym/ask_schools.svg)
](https://pypi.org/project/ask_schools/)
[![TravisCI](https://travis-ci.org/guinslym/ask_schools.svg?branch=master)](https://travis-ci.org/guinslym/ask_schools)
<hr/>

<p align="center">
  <img src="https://i.imgur.com/sJzfZsL.jpg" width="154">
  <h1 align="center">InstaPy</h1>
  <p align="center">Tooling that <b>automates</b> your social media interactions to “farm” Likes, Comments, and Followers on Instagram
Implemented in Python using the Selenium module.<p>
  <p align="center">
    <a href="https://github.com/timgrossmann/InstaPy/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/license-GPLv3-blue.svg" />
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
    <a href="https://travis-ci.org/timgrossmann/InstaPy">
	<img src="https://travis-ci.org/timgrossmann/InstaPy.svg?branch=master">
    </a>
    <a href="https://www.github.com/timgrossmann/InstaPy#backer">
	<img src="https://opencollective.com/instapy/backers/badge.svg">
    </a>
    <a href="https://www.github.com/timgrossmann/InstaPy#sponsors">
	<img src="https://opencollective.com/instapy/sponsors/badge.svg">
    </a>  
    <a href="https://discord.gg/FDETsht">
	<img src="https://img.shields.io/discord/510385886869979136.svg">
    </a>
  </p>
</p>



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

1.  Replace SMS with email to ASK SP inbox
2.  Add tests
3.  Add Docker
4.  Move the logic to create a Mobile app

