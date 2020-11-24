from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['item_base']
collection = db['item_collection']


# helpers
def item_helper(item) -> dict:
    return {
        'id': str(item['_id']),
        'title': str(item['title']),
        'description': str(item['description']),
        'parameters': item['parameters'],
    }


# create new item
def create_item(item_data: dict) -> dict:
    item = collection.insert_one(item_data)
    new_item = collection.find_one({'_id': item.inserted_id})
    return item_helper(new_item)


# retrieve item by ID
def retrieve_item_by_id(id: str) -> dict:
    # check valid ID
    if ObjectId.is_valid(id):
        item = collection.find_one({'_id': ObjectId(id)})
        return item_helper(item)
    else:
        return {'error': 'not valid id'}


# retrieve items by parameters
def retrieve_items_by_parameters(params: dict):
    items = []
    query = {}

    # формируем запрос из параметров
    for p in params:
        # проверяем, является ли параметр зарезервированным в нашей модели, если да,
        # то используем вхождение регулярного выражения
        if p in ['title', 'description']:
            query[p] = {'$regex': params[p]}
        else:
            query['parameters.' + p] = params[p]

    for item in collection.find(query, {"title": 1, "_id": 0}):
        items.append(item)
    return items
