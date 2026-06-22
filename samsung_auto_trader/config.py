import os
from dotenv import load_dotenv
from datetime import time

load_dotenv()

ACCOUNT = os.getenv("GH_ACCOUNT")
APPKEY = os.getenv("GH_APPKEY")
APPSECRET = os.getenv("GH_APPSECRET")

BASE_URL = "https://openapivts.koreainvestment.com:29443"

SYMBOL = "005930"

BUY_OFFSET = 1000
SELL_OFFSET = 1000

POLL_INTERVAL = 180

TRADING_START = time(9, 10)
TRADING_END = time(15, 30)
