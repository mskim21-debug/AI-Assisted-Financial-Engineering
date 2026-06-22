import json
import os
import requests
from datetime import datetime

from config import APPKEY, APPSECRET, BASE_URL
from logger import log

TOKEN_FILE = "token_cache.json"
TOKEN_URL = f"{BASE_URL}/oauth2/tokenP"


def load_token():
    if not os.path.exists(TOKEN_FILE):
        return None

    with open(TOKEN_FILE, "r") as f:
        data = json.load(f)

    if data.get("date") == str(datetime.now().date()):
        log("Using cached token")
        return data["token"]

    return None


def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        json.dump({"date": str(datetime.now().date()), "token": token}, f)


def get_token():
    token = load_token()
    if token:
        return token

    log("Requesting new token")

    r = requests.post(
        TOKEN_URL,
        json={
            "grant_type": "client_credentials",
            "appkey": APPKEY,
            "appsecret": APPSECRET,
        },
        timeout=10,
    )

    r.raise_for_status()
    token = r.json()["access_token"]

    save_token(token)
    return token
