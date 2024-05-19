from calculator import Calculator


class Area(Calculator):
    def __init__(self, number1, number2):
        super().__init__(number1, number2)

    def rectangle(self):
        return self.multiply()

    def triangle(self):
        return self.divide() / 2

    def circle(self):
        return self.multiply() * 3.1416
