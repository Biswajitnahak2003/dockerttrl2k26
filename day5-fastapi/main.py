from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to day5 + FastAPI",
        "author": "Biswajit"
    }

@app.get("/health")
def health():
    return{"status": "healthy"}
