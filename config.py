from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME", "TebKillerMusikbot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
