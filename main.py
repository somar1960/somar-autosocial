from fastapi import FastAPI

app = FastAPI(
    title="SOMAR AutoSocial",
    description="AI powered Instagram automation platform"
)

@app.get("/")
def home():
    return {
        "message": "SOMAR AutoSocial is running 🚀"
    }
