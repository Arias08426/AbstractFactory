from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def sellCar(self):
        pass