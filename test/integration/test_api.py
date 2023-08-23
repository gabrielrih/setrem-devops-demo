import requests

from typing import Dict, List
from http import HTTPStatus
from unittest import TestCase


class TestApi(TestCase):

    base_url = 'http://localhost:5000'

    # def test_insert_food(self):
    #     # Given
    #     data = {
    #         "name": "My food",
    #         "description": "This is the description",
    #         "link": "https://fake-link.com",
    #         "link_image": "https://fake-image-link.com"
    #     }
    #     # When
    #     endpoint = self.base_url + '/api/food/'
    #     headers = {
    #         'Content-Type': 'application/json'
    #     }
    #     response = requests.post(endpoint, data, headers)
    #     # Then
    #     print(response.json)
    #     print(response.content)
    #     print(response.reason)
    #     self.assertEqual(response.status_code, HTTPStatus.CREATED)
    #     self.assertEqual(response.content, [])

    def test_insert_food_when_content_type_not_allowed(self):
        # Given
        data = {
            "name": "any data"
        }
        invalid_header = {
            'Content-Type': 'application/pdf'
        }
        # When
        endpoint = self.base_url + '/api/food/'
        response = requests.post(endpoint, data, invalid_header)
        json = response.json()
        # Then
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(json, {})

    def test_insert_food_invalid_schema(self):
        pass

    def test_insert_food_when_body_is_empty(self):
        pass

    def test_get_food_by_name(self):
        pass

    # def test_get_all_foods(self):
    #     # When
    #     endpoint = self.base_url + '/api/food/'
    #     response = requests.get(endpoint)
    #     # Then
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     # self.assertIsNotNone(response.content)
