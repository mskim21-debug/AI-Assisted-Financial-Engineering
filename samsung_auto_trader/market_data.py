from api_client import APIClient
from config import BASE_URL, SYMBOL
from logger import log

client = APIClient()


def get_price():
    url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"

    params = {
        "fid_cond_mrkt_div_code": "J",
        "fid_input_iscd": SYMBOL,
    }

    r = client.get(url, params, tr_id="FHKST01010100")
    r.raise_for_status()

    price = int(r.json()["output"]["stck_prpr"])

    log(f"Price: {price}")
    return price
