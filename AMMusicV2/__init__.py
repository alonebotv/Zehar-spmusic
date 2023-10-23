from AMMusicV2.core.bot import Aviax
from AMMusicV2.core.dir import dirr
from AMMusicV2.core.git import git
from AMMusicV2.core.userbot import Userbot
from AMMusicV2.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
