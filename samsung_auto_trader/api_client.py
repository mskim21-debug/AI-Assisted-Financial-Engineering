import requests
from auth import get_token
from config import APPKEY, APPSECRET


class APIClient:

    def headers(self, tr_id):
        return {
            "authorization": f"Bearer {get_token()}",
            "appkey": APPKEY,
            "appsecret": APPSECRET,
            "tr_id": tr_id,
            "content-type": "application/json",
        }

    def get(self, url, params, tr_id):
        return requests.get(
            url,
            headers=self.headers(tr_id),
            params=params,
            timeout=10,
        )

    def post(self, url, body, tr_id):
        return requests.post(
            url,
            headers=self.headers(tr_id),
            json=body,
            timeout=10,
        )
