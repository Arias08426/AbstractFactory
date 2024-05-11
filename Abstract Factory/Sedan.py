from abc import ABC, abstractmethod

class Sedan(Car, ABC):
    @abstractmethod
    def SellCar(self):
        pass