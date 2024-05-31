from gadget import Gadget


class Laptop(Gadget):
    def __init__(self, brand, model, device_type, price, ram, cpu, screen_size):
        super().__init__(brand, model, device_type, price)
        self.ram: int = ram
        self.cpu: str = cpu
        self.screen_size: float = screen_size

    def get_info(self) -> object:
        return f'{self.brand} {self.model} {self.type} {self.price} {self.ram} {self.cpu} {self.screen_size}'


class Smartphone(Gadget):
    def __init__(self, brand, model, device_type, price, foldable):
        super().__init__(brand, model, device_type, price)
        self.foldable: bool = foldable

    def get_info(self) -> object:
        return f'{self.brand} {self.model} {self.type} {self.price} {self.foldable}'


iphone = Smartphone('Apple', 'iPhone 12', 'smartphone', 999, False)
zfold = Smartphone('Samsung', 'Galaxy Z Fold 2', 'smartphone', 1999, True)
macbook = Laptop('Apple', 'MacBook Pro', 'laptop', 3099, 16, 'M3 Max', 14)
g14 = Laptop('Asus', 'ROG Zephyrus G14', 'laptop', 1499, 32, 'Ryzen 9', 14)

print(iphone.get_info())
print(zfold.get_info())
print(macbook.get_info())
print(g14.get_info())
