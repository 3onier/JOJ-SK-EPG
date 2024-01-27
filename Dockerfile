FROM python:3
LABEL authors="3onier"

# install the software
RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

ADD src .

# create cronjob
RUN apt-get update && apt-get -y install cron
WORKDIR  /etc/cron.d
RUN crontab -l | { cat; echo "0 13 * * * /usr/local/bin/python3 /app/main.py -n 5 /out/epg.xmltv"; } | crontab -

# create an output
RUN mkdir /out
WORKDIR /out

CMD /usr/local/bin/python3 /app/main.py -n 5 /out/epg.xmltv ; cron -f
