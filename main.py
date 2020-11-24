from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from models import Item, response_item
from database import create_item, retrieve_item_by_id, retrieve_items_by_parameters

app = FastAPI(title='Item application')


# retrieve item by id
@app.get('/item/{item_id}')
async def get_item(item_id: str):
    return retrieve_item_by_id(item_id)


# retrieve items by parameters
@app.get('/items/')
async def get_items(request: Request):
    return retrieve_items_by_parameters(dict(request.query_params))


# create new item
@app.post('/item')
async def add_item(item: Item):
    new_item = create_item(jsonable_encoder(item))
    return response_item(new_item, 'New item inserted into DB')
