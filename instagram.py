import requests
from config import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID


def check_instagram_connection():
    url = f"https://graph.facebook.com/v21.0/{INSTAGRAM_ACCOUNT_ID}"

    params = {
        "fields": "username",
        "access_token": INSTAGRAM_ACCESS_TOKEN
    }

    response = requests.get(url, params=params)

    return response.json()
