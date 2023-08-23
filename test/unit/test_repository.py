import os

from unittest import TestCase
from pathlib import Path
from typing import List

from src.repository import InFileRepository


class Config(TestCase):
    def setUp(self):
        self.set_up_my_stuffs()

    def tearDown(self):
        self.tear_down_my_stuffs()


class TestInFileRepository(Config):

    __DATABASE_NAME = 'db_test.json'

    def __remove_db_file(self):
        file = Path(self.__DATABASE_NAME)
        if file.exists():
            os.remove(file)

    def set_up_my_stuffs(self):
        # Always remove the database file before run each test
        self.__remove_db_file()

    def tear_down_my_stuffs(self):
        self.__remove_db_file()

    def test_create_database(self):
        # Given / When
        repository = InFileRepository(self.__DATABASE_NAME)
        # Then
        file = Path(self.__DATABASE_NAME)
        self.assertTrue(file.exists())
        self.assertIsNotNone(repository)

    def test_insert_and_get_all_elements(self):
        # Given
        content = {
            "name": 'My name',
            "description": "My description"
        }
        # When
        repository = InFileRepository(self.__DATABASE_NAME)
        for _ in range(2):  # Insert the same element two times
            repository.insert(content)
        # Get inserted elements
        response = repository.get_all()
        # Then
        self.assertEqual(len(response), 2)  # Must have two elements
        self.assertIsInstance(response, List)  # The result must be a list

    def test_insert_and_get_elements_by_name(self):
        # Given
        repository = InFileRepository(self.__DATABASE_NAME)
        # When (Insert two different elements and then get them)
        repository.insert({
            "Name": "Key 1",
            "Value": "Value 1"
        })
        repository.insert({
            "Name": "Key 2",
            "Value": "Value 2"
        })
        response = repository.get_by_key(key='Name', value='Key 2')
        print(response)
        # Then
        self.assertEqual(len(response), 1)  # must found one element
        self.assertEqual(response[0]['Name'], "Key 2")  # check the Name key value
