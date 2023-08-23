from typing import List
from unittest import TestCase

from src.foods import Foods
from src.repository import InMemoryRepository


''' Test Foods class using InMemoryRepository '''
class TestFoods(TestCase):

    repository = InMemoryRepository()

    def test_get_all_foods(self):
        # Given
        foods = Foods(self.repository)
        # When
        data = foods.get_all()
        # Then
        self.assertIsNotNone(data)
        self.assertIsInstance(data, List)

    def test_add_and_get_food_by_name(self):
        # Given
        foods = Foods(self.repository)
        name = "My food"
        data = {
            "name": name,
            "description": "Description of the food"
        }
        # When
        foods.add_food(data)
        response = foods.get_food_by_name(name)
        # Then
        self.assertIsNotNone(response)
        self.assertEqual(response[0]['name'], name)
