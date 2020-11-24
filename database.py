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


# получить все товары из коллекции базы
def retrieve_item_by_parameters(params: dict = None):
    items = []
    query = {}
    # db.users.insert({"name": "Alex", "age": 28, company: {"name": "microsoft", "country": "USA"}})
    # db.users.find({"company.name": "microsoft"})
    #    {name: "Tom", age: 32}

    for p in params:
        # проверяем, является ли параметр зарезервированным в нашей модели
        if p in ['title', 'description']:
            query[p] = {'$regex': params[p]}
        else:
            query['parameters.' + p] = params[p]
    # print(query)
    for item in collection.find(query):
        items.append(item_helper(item))
    return items


# создать новый товар
def create_item(item_data: dict) -> dict:
    item = collection.insert_one(item_data)
    new_item = collection.find_one({'_id': item.inserted_id})
    # print('new_item', type(new_item), new_item)
    return item_helper(new_item)


# получить товар по ID
def retrieve_item_by_id(id: str) -> dict:
    item = collection.find_one({'_id': ObjectId(id)})
    if item:
        return item_helper(item)
