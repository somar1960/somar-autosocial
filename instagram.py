import requests
from config import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID


def check_instagram_connection():
    url = f"https://graph.facebook.com/v23.0/{INSTAGRAM_ACCOUNT_ID}"

    params = {
        "fields": "username",
        "access_token": INSTAGRAM_ACCESS_TOKEN
    }

    response = requests.get(url, params=params)

    return {
        "status_code": response.status_code,
        "data": response.json()
    }
