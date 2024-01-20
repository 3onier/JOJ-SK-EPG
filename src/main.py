from config.defaultChannels import JOJ
from helper.scheduleDownloader import download_schedule


if __name__ == '__main__':
    sche = download_schedule(JOJ, 2024, 1, 20)
    print(sche.getScheduleAsText())
