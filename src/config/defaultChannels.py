from classes.channel import Channel

PROGRAMM_URL = "https://www.joj.sk/tv-program"

JOJ = Channel("Joj.sk", "https://live.joj.sk/")
JOJ_PLUS = Channel("Joj-plus.sk", "https://plus.joj.sk/live")
JOJ_WAU = Channel("Joj-wau.sk", "https://wau.joj.sk/live")
JOJ_SPORT = Channel("Joj-sport.sk", "https:jojsport.joj.sk/")
JOJKO = Channel("Jojko.sk", "https://jojko.joj.sk/")
JOJ_CINEMA = Channel("Joj-cinama.sk", "http://jojcinema.cz/")

JOJ_GROUP = [
        JOJ,
        JOJ_PLUS,
        JOJKO,
        JOJ_CINEMA,
        JOJ_WAU,
        JOJ_SPORT
]
