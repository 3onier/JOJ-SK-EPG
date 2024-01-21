from typing import List, Self

from classes.media import Media
from classes.channel import Channel


class Schedule:
    channel: Channel
    media: list[Media] = []
    def __init__(self, channel: Channel):
        self.channel = channel

    def getScheduleAsText(self):
        """
        Returns the schedule in humand readable text form
        :return:
        """
        out = ""
        for m in self.media:
            out += f"{m.start_time} - {m.title}"
            out += '\n'
        return out

    def _sort(self):
        """
        Sort the Media in the schedule by datetime
        :return:
        """
        self.media.sort(key=lambda x: x.start_time)

    def merge(self, schedule: Self, sort=False) -> Self:
        """
        Merges two Scheduled into one and sorts the
        :param schedule: Schedule to be sorted with
        :param sort: Sorte them by Datetime
        :return:
        """
        if self.channel != schedule.channel:
            raise Exception("Channels of two Schedules must be the same to merge")
        self.media += schedule.media
        if sort:
            self._sort()
        return self

    def generate_end_time(self):
        """
        Generates the end time for each media by looking at the next value
        The Parser from the Website does not provide end time data, thus we must evaluate them by ourselves

        :return:
        """
        self._sort()
        new_media: list[Media] = []
        for m1, m2 in zip(self.media[0:-1], self.media[1:]):
            m1.end_time = m2.start_time
            new_media.append(m1)
        self.media = new_media
