import requests

from unittest import TestCase


class TestApi(TestCase):

    base_url = 'http://localhost:8080'

    def test_insert_food(self):
        pass

    def test_get_food_by_name(self):
        pass

    def test_get_all_foods(self):
        # Given
        endpoint = self.base_url + '/api/food/'
        # When
        response = requests.get(endpoint)
        print(response)
        # Then
        self.assertEqual(response, '')
