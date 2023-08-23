from typing import Dict, List
from marshmallow import Schema, fields

from src.repository import Repository, InFileRepository


class FoodSchema(Schema):
     name = fields.String(required=True)
     description = fields.String(required=True)
     link = fields.String(required=False)
     link_image = fields.String(required=False)


class Foods:
    def __init__(self, repository: Repository = InFileRepository()):
        self.repository = repository
        
    def add_food(self, content: Dict) -> Dict:
        self.repository.insert(content)
        return content

    def get_all(self) -> List:
        return self.repository.get_all()
    
    def get_food_by_name(self, food_name: str) -> List:
        return self.repository.get_by_key(key='name', value=food_name)
