from abc import ABC
from typing import Dict, List
from tinydb import TinyDB


class Repository(ABC):
    def __init__(self, database_name: str) -> None:
        pass

    def insert(self, content: Dict) -> None:
        pass

    def get_all(self) -> List:
        pass

    def get_by_key(self, key: str, value: str) -> List:
        pass


class InFileRepository(Repository):
    def __init__(self, database_name: str = 'db.json') -> None:
        self.db = TinyDB(database_name)

    def insert(self, content: Dict) -> None:
        self.db.insert(content)

    def get_all(self) -> List:
        return self.db.all()

    def get_by_key(self, key: str, value: str) -> List:
        response = []
        for item in self.get_all():
            if item.get(key) == value:
                response.append(item)
        return response


class InMemoryRepository(Repository):
    __database = []

    def __init__(self, database_name: str = 'db.json'):
        pass

    def insert(self, content: Dict) -> None:
        self.__database.append(content)

    def get_all(self) -> List:
        return self.__database

    def get_by_key(self, key: str, value: str) -> List:
        response = []
        for item in self.__database:
            if item.get(key) == value:
                response.append(item)
        return response
