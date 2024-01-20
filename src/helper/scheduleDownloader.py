from bs4 import BeautifulSoup

from datetime import datetime

from classes.channel import Channel
from classes.media import Media
from classes.schedule import Schedule
from config.defaultChannels import PROGRAMM_URL

import requests


def download_html(url: str):
    r = requests.get(url)
    return r.text


def download_schedule(channel: Channel, year:int, month:int, day:int):
    # css selector for the channel
    search_string: str = f"div.b-program[data-live-url=\"{channel.live_url}\"] div.e-program"
    html = download_html(PROGRAMM_URL)
    soup = BeautifulSoup(html, 'html.parser')

    # now create
    e_programs = soup.select(search_string)

    media = []
    for e_program in e_programs:
        # parse time
        time_string = e_program.select("div.e-bar")[0]['data-playtime'].split(" ")[0]
        start_time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S%z") #%d/%m/%y %H:%M:%S.%f

        # parse title and thumbnail
        thumbnail_url = e_program['data-image']
        title = e_program.select("span.title")[0].getText(strip=True)

        media.append(Media(title, start_time, thumbnail_url))

    schedule = Schedule(channel)
    schedule.media = media
    return schedule