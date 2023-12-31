import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","12227067"))
API_HASH = getenv("API_HASH","b463bedd791aa733ae2297e6520302fe")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_USERNAME = getenv("OWNER_USERNAME","AM_YTBOTT")
ABOUT_ME = getenv("ABOUT_ME","https://t.me/About_AMBot")
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.pom3ops.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999"))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001840241140"))
CHAT_LOGS = int(getenv("CHAT_LOGS", "-1001841879487"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5097836954"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AbhiModszYT/AMMusicV2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","https://t.me/AMBOTYT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/AM_YTSUPPORT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
STATS_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
STREAM_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/65c35ede2f14baafaaf77.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
