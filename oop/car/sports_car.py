from car import Car


class SportsCar(Car):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed

    def rev_car(self):
        print("Car is revving")
