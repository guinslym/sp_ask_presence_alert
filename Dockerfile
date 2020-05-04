FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python 

RUN  apt-get install -y cron

# copy current directory to app
# the proper credentials for Twillio in .env needs to be installed
COPY . /app
WORKDIR /app

# Run WITHOUT cronjob
RUN pip3 install -r requirements.txt
RUN python3 /app/sp_ask_service_availability_alert.py 

#Run with cronjob
#ADD crontab-example /etc/cron.d/hello-cron
#RUN chmod 0644 /etc/cron.d/hello-cron
#RUN touch /var/log/cron.log
#CMD cron && tail -f /var/log/cron.log

#ENTRYPOINT /entrypoint.sh