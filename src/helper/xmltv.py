from bs4 import BeautifulSoup

from classes.channel import Channel
from classes.media import Media
from classes.schedule import Schedule


class Xmltv:
    program_tags: BeautifulSoup
    channel_tags: BeautifulSoup

    schedules: list[Schedule]

    def __init__(self, schedules: list[Schedule]):
        self.program_tags = BeautifulSoup()
        self.channel_tags = BeautifulSoup()
        self.schedules = schedules
        self.generate()

    def __str__(self):
        out = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE tv SYSTEM "xmltv.dtd">\n'
        soup = BeautifulSoup()
        tv_tag = soup.new_tag("tv")
        tv_tag['generator-info-name'] = "3onier-JOJ-SK-EPG"
        tv_tag.append(self.channel_tags)
        tv_tag.append(self.program_tags)
        soup.append(tv_tag)
        return out + str(soup)

    def _create_channel_tag(self, channel: Channel):
        """
        Creats a channel tag based on channel
        :param channel:
        :return:
        """
        soup = BeautifulSoup()
        tag = soup.new_tag("channel", attrs={
            'id': channel.channel_name
        })
        display_name_tag = soup.new_tag("display-name")
        display_name_tag.append(soup.new_string(channel.channel_name))
        tag.append(display_name_tag)
        self.channel_tags.append(tag)

    def _create_channel_tags(self):
        for schedule in self.schedules:
            self._create_channel_tag(schedule.channel)

    def _create_program_tag(self, channel: Channel, media: Media):
        soup = BeautifulSoup()
        tag = soup.new_tag("programme", attrs={
            'channel': channel.channel_name,
            'start': media.get_start_time_str(),
            'stop': media.get_end_time_str()
        })
        title_tag = soup.new_tag("title", attrs={
            'lang': 'sk'
        })
        title_tag.append(soup.new_string(media.title))

        thumbnail_tag = soup.new_tag("icon", attrs={
            'src': media.thumbnail_url
        })

        tag.append(title_tag)
        self.program_tags.append(tag)

    def _create_program_tags(self, schedule: Schedule):
        for media in schedule.media:
            self._create_program_tag(schedule.channel, media)

    def _create_programs_tags(self):
        for schedule in self.schedules:
            self._create_program_tags(schedule)

    def generate(self):
        self._create_programs_tags()
        self._create_channel_tags()

    def saveXMLTV(self, filename: str):
        self.generate()
        with open(filename, 'w') as f:
            f.write(str(self))
