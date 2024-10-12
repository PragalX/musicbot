from AashikaMusicBot.core.bot import AashikaMusicBot
from AashikaMusicBot.core.dir import dirr
from AashikaMusicBot.core.git import git
from AashikaMusicBot.core.userbot import Userbot
from AashikaMusicBot.misc import dbb, heroku
from .spotify import SpotifyAPI

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AashikaMusicBot()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
