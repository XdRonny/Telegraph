import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "7286754").strip()
API_HASH = os.getenv("API_HASH", "ea32d6cdb32f751aca22f05fdea1d3a8").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6155385003:AAFFjnpIA7ApWLi63ImlP2yk7_TCX36ph2s").strip()
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://Anjani:Anjani@cluster0.421tvtn.mongodb.net/?retryWrites=true&w=majority").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "TheBotHub")
LOG_ID = int(os.getenv("LOG_ID", "-1001862524511"))

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not MONGO_DB_URI:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
if not LOG_ID:
    print("No Log group defined...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit
