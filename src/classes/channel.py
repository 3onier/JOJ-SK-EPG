from classes.media import Media


class Channel:

    channel_name: str = ""
    live_url: str = ""

    def __init__(self, channel_name: str, live_url: str):
        """

        :param channel_name: Name of the Channel to map it to TVXML
        :param live_url: This is used as a unqualified selector for the HTML elements
        """
        self.channel_name = channel_name
        self.live_url = live_url
