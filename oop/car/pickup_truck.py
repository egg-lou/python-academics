from car import Car


class PickupTruck(Car):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    @staticmethod
    def towing():
        print("Truck is towing")
