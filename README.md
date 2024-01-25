# JOJ-Group EPG XMLTV Crawler
This projects provides and automated service to craw the EPG-Data from the Channels of the https://www.joj.sk/tv-program JOJ-SK-Group and format them into an TVXML file to parse it into [Plex](https://www.plex.tv/), [Jellyfin](https://jellyfin.org/) or [Emby](https://emby.media/).

## Limitations
- The data provided on the Website are limited, there is not much info about the number of Episode or Season no data regarding parental controll, language of the content (but it is usually slovak) or genre.
- The File has been only tested on Jellyfin

## Usage
### Requirements

- beautifulsoup4 >= 4.12.3
- requests >= 2.31.0

### Local
```
git clone https://github.com/3onier/JOJ-SK-EPG.git
cd JOJ-SK-EPG
python src/main.py [-n days to crawl < 6] filename
```
The command creates a file containing all the EPG-data.
### Docker
WIP
