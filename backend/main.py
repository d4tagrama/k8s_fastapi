from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    number: int

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/add")
def read_item(item: Item):
    item_dict = item.dict()

    return {"next_number": item.number+1}
