from datetime import datetime


class Media:

    title: str
    thumbnail_url: str
    start_time: datetime = None
    end_time: datetime

    def __init__(self, title: str, time_start: datetime, thumbnail_url: str = "", end_time: datetime = None):
        self.title = title
        self.start_time = time_start
        self.thumbnail_url = thumbnail_url
        self.end_time = end_time

    def get_start_time_str(self) -> str:
        return self.start_time.strftime("%Y%m%d%H%M%S %z")

    def get_end_time_str(self) -> str:
        if not self.end_time:
            raise Exception("No end time provided")
        return self.end_time.strftime("%Y%m%d%H%M%S %z")
