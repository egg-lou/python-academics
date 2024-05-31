class Products:
    def __init__(self, name, description, price, quantity, expiration):
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity
        self.expiration: str = expiration
        print(f"Added Product: {self.name}  {self.description}  {self.price} {self.quantity} "
              f"{self.expiration}\n")


class Cars:
    def __init__(self, brand, model, year, price, color):
        self.brand: str = brand
        self.model: str = model
        self.year: str = year
        self.price: float = price
        self.color: str = color
        print(f"Added Car: {self.brand} {self.model} {self.year} {self.price} {self.color}\n")


class Animals:
    def __init__(self, name, specie, age, weight, height):
        self.name: str = name
        self.specie: str = specie
        self.age: int = age
        self.weight: float = weight
        self.height: float = height
        print(f"Animal: {self.name} Specie: {self.specie} Age: {self.age} Weight: {self.weight} "
              f"Height: {self.height}\n")


product = Products("Toothpaste", "For brushing teeth", 50, 20, "2021-12-31")
car = Cars("Toyota", "Corolla", 2021, 20000, "White")
animal = Animals("Dog", "Canis lupus familiaris", 2, 5.5, 0.5)
