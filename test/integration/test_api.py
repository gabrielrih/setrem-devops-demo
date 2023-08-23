import requests

from typing import Dict, List
from http import HTTPStatus
from unittest import TestCase


class TestApi(TestCase):

    base_url = 'http://localhost:5000'

    def test_insert_food(self):
        # Given
        data = {
            "name": "My food",
            "description": "This is the description",
            "link": "https://fake-link.com",
            "link_image": "https://fake-image-link.com"
        }
        # When
        endpoint = self.base_url + '/api/food/'
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(endpoint, data, headers)
        # Then
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.content, [])

    def test_get_food_by_name(self):
        pass

    def test_get_all_foods(self):
        # When
        endpoint = self.base_url + '/api/food/'
        response = requests.get(endpoint)
        # Then
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsNotNone(response.content)
