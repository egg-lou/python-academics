def add(*args):
    for i in args: 
        i += i 
    
    return i

print(add(2, 4, 5))
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} lives in {value}")


print_address(name="John", address="New York", age=25, phone="1234567890")
print()

def print_order(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for key, value in kwargs.items():
        print(f"{key} = {value}")
    

print_order("Rafael Louie", "Villar", "Miguel", payment="Cash on Delivery", address="South Korea", number="1234567890", order="Pizza", delivery_attempts=0)