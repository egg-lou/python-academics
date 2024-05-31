class Products:
    name: str = "Milk"
    description: str = "Lactose-free milk"
    price: float = 50
    quantity: int = 20
    expiration: str = "2021-12-31"


class Cars:
    brand: str = "Porsche"
    model: str = "911"
    year: int = 2021
    price: float = 200000
    color: str = "Black"


class Animals:
    name: str = "Cat"
    specie: str = "Felis catus"
    age: int = 1
    weight: float = 2.5
    height: float = 0.25


animal = Animals()
car = Cars()
product = Products()
print(f"Product: {product.name} Description: {product.description} Price: {product.price} Quantity: {product.quantity} "
      f"Expiration: {product.expiration}\n")
print(f"Car: {car.brand} Model: {car.model} Year: {car.year} Price: {car.price} Color: {car.color}\n")
print(f"Animal: {animal.name} Specie: {animal.specie} Age: {animal.age} Weight: {animal.weight}"
      f"Height: {animal.height}\n")
