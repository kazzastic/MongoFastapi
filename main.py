from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if(item.name == "kazim"):
        new_name = item.name + " raza"
        item_dict.update({"full_name":new_name})
    return item_dict