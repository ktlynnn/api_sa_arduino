from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.db import read_data
import uvicorn

app = FastAPI(title="test")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "yawa!"}

@app.get("/v1/send/data")
def read_temp(temp: float, humidity: float):
        read_data(temp, humidity)
        return {"message": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.254", port=8000, log_level="info")