import time
from market_data import get_price
from account import get_holdings
from orders import buy, sell
from config import BUY_OFFSET, SELL_OFFSET
from logger import log


def run_cycle():

    price = get_price()
    before = get_holdings()

    buy_price = price - BUY_OFFSET
    sell_price = price + SELL_OFFSET

    buy(1, buy_price)

    if before["qty"] > 0:
        sell(before["qty"], sell_price)

    time.sleep(5)

    after = get_holdings()

    if after["qty"] > before["qty"]:
        log("BUY EXECUTED")
    elif after["qty"] < before["qty"]:
        log("SELL EXECUTED")
    else:
        log("NO CHANGE")
