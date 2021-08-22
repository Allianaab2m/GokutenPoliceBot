from os import getenv

from dotenv import load_dotenv

load_dotenv()

# get token from .env
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")

# bot profile
BOT_PREFIX = "gp."

SPREADSHEET_KEY = '12l3Fn5R_xU836y1Q877VpzPFj6yj4xPyNEuqIXdNf5o'

NG_WORD = getenv("NG_WORD")