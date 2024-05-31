from animal import Animal


class Lion(Animal):
    def __init__(self, name, age, weight, pack_leader):
        super().__init__(name, age, weight)
        self.pack_leader: bool = pack_leader

    def make_sound(self):
        print(f"{self.name} roars")

    def move(self):
        print(f"{self.name} walks")


class Cat(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed: str = breed

    def make_sound(self):
        print(f"{self.name} meows")

    def move(self):
        print(f"{self.name} runs")


cLion = Lion("Simba", 5, 200, True)
cLion.make_sound()
cLion.move()

cCat = Cat("Tom", 3, 10, "Persian")
cCat.make_sound()
cCat.move()
