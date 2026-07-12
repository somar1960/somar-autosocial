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


@app.get("/instagram-test")
def instagram_test():
    return check_instagram_connection()
