"""
This module implements the repository design pattern
"""
from abc import ABC, abstractmethod


class IRepository(ABC):
    """
    Interface for the repository
    """
    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass


class SQLModelRepository(IRepository):
    """
    Implementation of the repository using SQLModel
    """
    def get_item(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class InMemoryRepository(IRepository):
    """
    Implementation of the repository in memory
    """
    def __init__(self) -> None:
        self.__data_source = []

    def get_item(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class SQLAlchemyRepository(IRepository):
    """
    Implementation of the repository using SQLAlchemy
    """
    def get_item(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class PonyRepository(IRepository):
    """
    Implementation of the repository using Pony
    """
    def get_item(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class Main:
    """
    Entry point of the program
    """
    @staticmethod
    def run(repository: IRepository = None) -> None:
        print("Programa iniciado")


if __name__ == "__main__":
    Main.run()
