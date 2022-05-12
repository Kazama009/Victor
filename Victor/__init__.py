import time
import logging

from aiohttp import ClientSession
from Python_ARQ import ARQ

from Victor.config import Config

from pyrogram import Client

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)

START_TIME = time.time()

API_ID = Config.API_ID
API_HASH = Config.API_HASH

aiohttpsession = ClientSession()
arq = ARQ("https://arq.hamker.in", "YIECCC-NAJARO-OLLREW-SJSRIP-ARQ", aiohttpsession)

victor = Client(
    "Victor",
    api_id=API_ID,
    api_hash=API_HASH,
)

victor_version = "1.0.0"