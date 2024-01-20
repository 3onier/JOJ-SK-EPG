from classes.media import Media
from classes.channel import Channel


class Schedule:
    media: Media = []
    def __init__(self, channel: Channel):
        pass

    def getScheduleAsText(self):
        out = ""
        for media in self.media:
            out += f"{media.start_time} - {media.title}"
            out += '\n'
        return out