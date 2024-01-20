from datetime import datetime


class Media:
    def __init__(self, title: str, time_start: datetime, thumbnail_url: str = ""):
        self.title = title
        self.start_time = time_start
        self.thumbnail_url = thumbnail_url
