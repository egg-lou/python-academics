from abc import ABC, abstractmethod


class Gadget(ABC):
    def __init__(self, brand, model, device_type, price):
        self.brand: str = brand
        self.model: str = model
        self.type: str = device_type
        self.price: str = price

    @abstractmethod
    def get_info(self) -> object:
        pass
