from config.defaultChannels import JOJ, JOJ_PLUS
from helper.scheduleDownloader import download_schedule_for_n_day


if __name__ == '__main__':
    sche = download_schedule_for_n_day(JOJ, 2)
    print(sche.getScheduleAsText())