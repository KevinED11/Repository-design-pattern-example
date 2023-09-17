from abc import ABC, abstractmethod


class IRepository(ABC):
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
    def get_item(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class InMemoryRepository(IRepository):
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
    def get_item(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class PonyRepository(IRepository):
    def get_item(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class Main:
    @staticmethod
    def run(repository: IRepository = None) -> None:
        print("Programa iniciado")


if __name__ == "__main__":
    Main.run()
