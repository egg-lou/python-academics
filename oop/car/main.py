from sports_car import SportsCar
from pickup_truck import PickupTruck

# Create a sports car
Porsche = SportsCar("Porche", "911", 2020, 200)
Porsche.display()
Porsche.start()
Porsche.rev_car()

# Create a pickup truck
Ford = PickupTruck("Ford", "F150 Raptor", 2020, 5000)
Ford.display()
Ford.start()
Ford.towing()
