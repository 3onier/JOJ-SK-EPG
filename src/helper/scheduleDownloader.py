from functools import lru_cache

from bs4 import BeautifulSoup

from datetime import datetime, timedelta

from classes.channel import Channel
from classes.media import Media
from classes.schedule import Schedule
from config.defaultChannels import PROGRAMM_URL

import requests


@lru_cache()
def download_html(url: str) -> str:
    r = requests.get(url)
    return r.text


def generate_url(year: int, month: int, day: int):
    return f"{PROGRAMM_URL}/den-{day}-{month}-{year}"


def download_schedule_by_day(channel: Channel, year: int, month: int, day: int) -> Schedule:
    """
    Crawls the Schedule by the Date and channel given
    :param channel:
    :param year:
    :param month:
    :param day:
    :return: Schedule object
    """
    # css selector for the channel
    search_string: str = f"div.b-program[data-live-url=\"{channel.live_url}\"] div.e-program"
    html = download_html(generate_url(year, month, day))
    soup = BeautifulSoup(html, 'html.parser')

    # now create
    e_programs = soup.select(search_string)

    media = []
    for e_program in e_programs:
        # parse time
        time_string = e_program.select("div.e-bar")[0]['data-playtime'].split(" ")[0]
        start_time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S%z")  # %d/%m/%y %H:%M:%S.%f

        # parse title and thumbnail
        thumbnail_url = e_program['data-image']
        title = e_program.select("span.title")[0].getText(strip=True)

        media.append(Media(title, start_time, thumbnail_url))

    schedule = Schedule(channel)
    schedule.media = media
    return schedule


def download_schedule_for_n_day(channel: Channel, n: int):
    """
    Crawls the Schdule for the next n day
    :param channel: Channal being craweld
    :param n: amount of days being craweld
    :return:
    """
    if n > 5:
        raise Exception("Cannot craw more then 5 days")

    schedule = Schedule(channel)
    # the site has some weird behavior of having the date break at around 5pm, this can be ignored when crawling one day
    # in the past
    today = datetime.now() - timedelta(days=1)
    for i in range(n):
        date = today + timedelta(days=1 * i)
        year = int(date.year)
        month = int(date.month)
        day = int(date.day)
        schedule.merge(download_schedule_by_day(channel, year, month, day))
    schedule.generate_end_time()
    return schedule


def download_schedules_for_n_days(channels: list[Channel], n: int):
    """
    Crawl the schedules for multiple channels and return as list of schedules
    :param channels:
    :param n:
    :return:
    """
    schedules:list[Schedule] = []
    for channel in channels:
        s = download_schedule_for_n_day(channel, n)
        schedules.append(s)
    return schedules