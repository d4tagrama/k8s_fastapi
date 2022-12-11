import requests
import json
from typing import Union

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/number/{number}")
def read_item(number: int):
    backend_endpoint = 'http://srv-backend:8180/add/'
    post_response = requests.post( backend_endpoint, json={"number": number })
    print(post_response.text)
    return post_response.json()
