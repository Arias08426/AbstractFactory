from abc import ABC, abstractmethod

class CarFactory(ABC):

    @abstractmethod
    def create_suv(self):
        pass

    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_hatchback(self):
        pass
