class Car:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    @staticmethod
    def start():
        print("Car has started")

    @staticmethod
    def stop():
        print("Car has stopped")