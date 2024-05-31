from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, age, weight):
        self.name: str = name
        self.age: int = age
        self.weight: float = weight

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
