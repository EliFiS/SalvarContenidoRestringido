#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22250695
API_HASH = "6b95376fb49d377f70206b3f1a7ec491"
BOT_TOKEN = "5086036634:AAFpRFQV4NEIzg8fEotiOadKOWIqQQl6rQE"
SESSION = "AQC2AgVSlkYEhnBSqnYWhTOP0mTN0XSjg2zArOsn3-EmFoUykx5pHxCAsOkiU5Krtd4SEbRypaJGDtvMciKRNTTj3uDrw7jBYM4GHD3PJZUyxO3AsxtG9v6JMrLFfT_bK5prnaVF8qeURtRUVtNXsIWCCa2Qa4A1WhWFJswO9cBu7Xt3sE9O15AVXyLEvzHpdpIPOF9_XgKz4l_YKpwLR-_E489R8tnnoVEMKx77eVHN9RUlO9pNa7ScgfXIitfHw4snczcKhO5QLYdoAoXDzvwj9N_UZU195NkmilRmiBMIboUIdKOySBHwZsqXVEPCPNF09xFZ_b-t2fN7h8eGvnsCAAAAAVfGba8A"
FORCESUB = "EliFiS_Official_SaveRestricted"
AUTH = 593171886

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("¡Error del bot de usuario! ¿Ha agregado SESSION durante la implementación?")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
