from fastapi import FastAPI
from config import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID

app = FastAPI(
    title="SOMAR AutoSocial"
)

@app.get("/")
def home():
    return {
        "message": "SOMAR AutoSocial is running 🚀"
    }

@app.get("/check-config")
def check_config():
    return {
        "token_exists": bool(INSTAGRAM_ACCESS_TOKEN),
        "token_start": INSTAGRAM_ACCESS_TOKEN[:2] if INSTAGRAM_ACCESS_TOKEN else None,
        "account_id_exists": bool(INSTAGRAM_ACCOUNT_ID)
    }
