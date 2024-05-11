from abc import ABC, abstractmethod

class Suv(Car, ABC):
    @abstractmethod
    def SellCar(self):
        pass