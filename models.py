from typing import List
from pydantic import BaseModel, Field


# item model
class Item(BaseModel):
    title: str
    description: str
    parameters: List[dict] = []

    class Config:
        schema_extra = {
            "example": {
                "title": "Nokia 3310",
                "description": "cellphone Nokia",
                "parameters": [
                    {"model": "3310"},
                    {"batery": "800"}
                ]
            }
        }


def response_item(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }
