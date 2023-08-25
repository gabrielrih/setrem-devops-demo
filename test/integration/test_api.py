import requests
import json


from http import HTTPStatus
from unittest import TestCase


class TestFoodApi(TestCase):

    # This is the aliases used on docker compose
    # So, to run the test integration please use the docker compose
    endpoint = 'http://my-ip.dev:5000/api/food/'
    headers = {
        'Content-Type': 'application/json'
    }

    def test_insert_and_get_food_by_name(self):
        # Given
        name = "My food"
        data = {
            "name": name,
            "description": "This is the description",
            "link": "https://fake-link.com",
            "link_image": "https://fake-image-link.com"
        }
        # When
        # Inserting food
        post_response = requests.post(url=self.endpoint,
                                      data=json.dumps(data),
                                      headers=self.headers)
        # Getting food by name
        params = {
            "name": "My food"
        }
        get_response = requests.get(url=self.endpoint, params=params)

        # Then
        # Validation for the POST method
        self.assertEqual(post_response.status_code, HTTPStatus.CREATED)
        self.assertEqual(post_response.json()['name'], data['name'])
        # Validation for the GET method
        self.assertEqual(get_response.status_code, HTTPStatus.OK)
        self.assertEqual(len(get_response.json()), 1)  # Must return one element

    def test_insert_food_when_content_type_not_allowed(self):
        # Given
        data = {
            "name": "any data"
        }
        invalid_header = {
            'Content-Type': 'application/pdf'
        }
        expected_error_message = 'Content-Type application/pdf not supported! Must be application/jso'
        # When
        response = requests.post(url=self.endpoint,
                                 data=data,
                                 headers=invalid_header)
        # Then
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        error_message = response.json()
        error_message = error_message['error']['message']
        self.assertEqual(error_message, expected_error_message)

    def test_insert_food_invalid_schema(self):
        # Given
        invalid_data = {
            "id": "123",
            "number": "999"
        }
        expected_error_message = 'Invalid schema! Failed to parse it.'
        # When
        response = requests.post(url=self.endpoint,
                                 data=invalid_data,
                                 headers=self.headers)
        # Then
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        error_message = response.json()
        error_message = error_message['error']['message']
        self.assertEqual(error_message, expected_error_message)

    def test_insert_food_when_body_is_empty(self):
        # Given
        empty_data = {}
        expected_error_message = 'Body cannot be empty!'
        # When
        response = requests.post(url=self.endpoint,
                                 data=empty_data,
                                 headers=self.headers)
        # Then
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        error_message = response.json()
        error_message = error_message['error']['message']
        self.assertEqual(error_message, expected_error_message)

    def test_get_all_foods(self):
        # When
        response = requests.get(self.endpoint)
        # Then
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertGreaterEqual(len(response.json()), 1)  # Must have at least one food on the db
