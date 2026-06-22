from api_client import APIClient
from config import BASE_URL, ACCOUNT
from logger import log

client = APIClient()


def get_holdings():
    url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/inquire-balance"

    params = {
        "CANO": ACCOUNT[:8],
        "ACNT_PRDT_CD": ACCOUNT[8:],
        "AFHR_FLPR_YN": "N",
        "OFL_YN": "",
        "INQR_DVSN": "02",
        "UNPR_DVSN": "01",
        "FUND_STTL_ICLD_YN": "N",
        "FNCG_AMT_AUTO_RDPT_YN": "N",
        "PRCS_DVSN": "00",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": "",
    }

    r = client.get(url, params, tr_id="VTTC8434R")
    r.raise_for_status()

    data = r.json()

    qty = 0
    cash = int(data["output2"]["dnca_tot_amt"])

    for item in data["output1"]:
        if item["pdno"] == "005930":
            qty = int(item["hldg_qty"])

    result = {"qty": qty, "cash": cash}

    log(f"Holdings: {result}")
    return result
