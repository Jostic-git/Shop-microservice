from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from models import Item, response_item
from database import create_item, retrieve_item_by_id, retrieve_item_by_parameters

app = FastAPI(title='Item application')


# get item's list
@app.get('/item/{item_id}')
async def get_item(item_id: str):
    item = retrieve_item_by_id(item_id)
    if item:
        return item
    else:
        return response_item(None, 'Ничего не нашли')


@app.get('/items/')
async def get_items(request: Request):
    return retrieve_item_by_parameters(dict(request.query_params))


# создает новый товар
@app.post('/item')
async def add_item(item: Item):
    new_item = create_item(jsonable_encoder(item))
    return response_item(new_item, 'item inserted into DB')
