from unittest import TestCase
from src.foods import Foods


class TestFoods(TestCase):
    def test_get_favorites(self):
        # Given
        # When
        foods = Foods.get_favorites()
        # Then
        self.assertIsNotNone(foods)
        self.assertIsInstance(foods, dict)