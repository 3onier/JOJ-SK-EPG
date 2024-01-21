from config import defaultChannels
from helper.scheduleDownloader import download_schedules_for_n_days
from helper.xmltv import Xmltv

import argparse

parser = argparse.ArgumentParser(
    prog="JOJ-SK EPG Crawler",
    description="This program craws the publicly available data from https://www.joj.sk/tv-program/ and creates and XMLTV-file ",
)
parser.add_argument('filename',
                    help="filename of the output XMLTV-file",
                    type=str
                    )
parser.add_argument("-n",
                    "--number_days",
                    help="number of days to craws <= 5",
                    default=3,
                    type=int,
                    )

if __name__ == '__main__':
    args = parser.parse_args()
    sche = download_schedules_for_n_days(defaultChannels.JOJ_GROUP, args.number_days)
    xmltv = Xmltv(sche)
    print(xmltv)
    xmltv.saveXMLTV(args.filename)
