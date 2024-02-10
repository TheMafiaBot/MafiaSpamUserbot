import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    API_ID = os.environ.get("API_ID", 2184829)
    API_HASH = os.environ.get("API_HASH", "6930b92388baabff4cb4a1d377085035")
    SESSION_ONE = os.environ.get("SESSION_ONE", None)
    SESSION_TWO = os.environ.get("SESSION_TWO", None)
    SESSION_THREE = os.environ.get("SESSION_THREE", None)
    SESSION_FOUR = os.environ.get("SESSION_FOUR", None)
    SESSION_FIVE = os.environ.get("SESSION_FIVE", None)
    BOT_TOKEN  = os.environ.get("BOT_TOKEN", None)
    BOT_USERNAME  = os.environ.get("BOT_USERNAME", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    OWNER_NAME = os.environ.get("OWNER_NAME", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
    CO_OWNER_ID = set(int(x) for x in os.environ.get("CO_OWNER_ID", None).split())
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", None).split())
    HEROKU_APP_ID = os.environ.get("HEROKU_APP_ID", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    DISPLAY_PIC = os.environ.get("DISPLAY_PIC", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)
    CMD_HANDLER = os.environ.get("CMD_HANDLER", ".")
