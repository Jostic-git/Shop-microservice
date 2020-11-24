from typing import List
from pydantic import BaseModel, Field


# класс товар
class Item(BaseModel):
    title: str = (...)
    description: str = (...)
    parameters: List[dict] = []

    class Config:
        schema_extra = {
            "example": {
                "title": "Nokia 3310",
                "description": "cellphone nokia",
                "parameters": [
                    {"model": "3310"},
                    {"batary": "800 mAh"}
                ]
            }
        }


def response_item(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }


def error_response_item(error, code, message):
    return {'error': error, 'code': code, 'message': message}
