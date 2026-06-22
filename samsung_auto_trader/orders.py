from api_client import APIClient
from config import BASE_URL, ACCOUNT, SYMBOL
from logger import log

client = APIClient()


def buy(qty, price):
    log(f"BUY order qty={qty} price={price}")

    url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/order-cash"

    body = {
        "CANO": ACCOUNT[:8],
        "ACNT_PRDT_CD": ACCOUNT[8:],
        "PDNO": SYMBOL,
        "ORD_DVSN": "00",
        "ORD_QTY": str(qty),
        "ORD_UNPR": str(price),
    }

    r = client.post(url, body, tr_id="VTTC0802U")
    r.raise_for_status()
    return r.json()


def sell(qty, price):
    log(f"SELL order qty={qty} price={price}")

    url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/order-cash"

    body = {
        "CANO": ACCOUNT[:8],
        "ACNT_PRDT_CD": ACCOUNT[8:],
        "PDNO": SYMBOL,
        "ORD_DVSN": "00",
        "ORD_QTY": str(qty),
        "ORD_UNPR": str(price),
    }

    r = client.post(url, body, tr_id="VTTC0801U")
    r.raise_for_status()
    return r.json()
