from classes.media import Media


class Channel:

    media: Media = []

    def __init__(self, channel_name: str, live_url: str):
        self.channel_name = channel_name
        self.live_url = live_url
