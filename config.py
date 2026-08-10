from os import getenv
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = getenv("DISCORD_TOKEN")
BOT_OWNER_ID = int(getenv("BOT_OWNER_ID"))
USER_A_ID = int(getenv("USER_A_ID"))
USER_B_ID = int(getenv("USER_B_ID"))
USER_C_ID = int(getenv("USER_C_ID"))
USER_D_ID = int(getenv("USER_D_ID"))
USER_F_ID = int(getenv("USER_F_ID"))
USER_G_ID = int(getenv("USER_G_ID"))
CHANNEL_ID = int(getenv("CHANNEL_ID"))
