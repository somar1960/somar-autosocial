from fastapi import FastAPI
from instagram import check_instagram_connection

app = FastAPI(
    title="SOMAR AutoSocial",
    description="AI powered Instagram automation platform"
)

@app.get("/")
def home():
    return {
        "message": "SOMAR AutoSocial is running 🚀"
    }

@app.get("/check-config")
def check_config():
    from config import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID

    return {
        "token_exists": bool(INSTAGRAM_ACCESS_TOKEN),
        "token_start": INSTAGRAM_ACCESS_TOKEN[:2] if INSTAGRAM_ACCESS_TOKEN else None,
        "account_id_exists": bool(INSTAGRAM_ACCOUNT_ID)
    }

@app.get("/instagram-test")
def instagram_test():
    return check_instagram_connection()
