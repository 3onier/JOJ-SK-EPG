from config import defaultChannels
from helper.scheduleDownloader import download_schedules_for_n_days
from helper.xmltv import Xmltv


if __name__ == '__main__':
    sche = download_schedules_for_n_days(defaultChannels.JOJ_GROUP,2)
    xmltv = Xmltv(sche)
    print(xmltv)
