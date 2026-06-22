import time
from datetime import datetime

from trader import run_cycle
from config import TRADING_START, TRADING_END, POLL_INTERVAL
from logger import log


def in_window():
    now = datetime.now().time()
    return TRADING_START <= now <= TRADING_END


def main():

    log("Trading bot started")

    while True:

        now = datetime.now().time()

        if now > TRADING_END:
            log("Trading ended")
            break

        if not in_window():
            time.sleep(30)
            continue

        run_cycle()
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
