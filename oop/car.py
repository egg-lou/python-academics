class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("Driving a " + self.make + " " + self.model)

    def stop(self):
        print("Stopping the " + self.color + " " + self.make)