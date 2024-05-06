def purchase_info(name, item_name, quantity, price, cash):
    total_price = quantity * price
    if total_price >= 1000:
        total_price *= 0.7 
    change = cash - total_price

    print(f'Customer Name: {name}')
    print(f'Purchased Item: {item_name}')
    print(f'Quantity: {quantity}') 
    print(f'Price: {price}')
    print(f'Total Price: {total_price}')
    print(f'Cash: {cash}')
    print(f'The Total Bill is: {total_price}')
    print(f'The Change is: {change}')

if __name__ == '__main__':
    while True:
        try: 
            name = input('Enter your name: ')
            item_name = input('Enter the item name: ')
            quantity = int(input('Enter the quantity: '))
            price = float(input('Enter the price: '))
            cash = float(input('Enter the cash: '))

            purchase_info(name, item_name, quantity, price, cash)
            break

        except ValueError:
            print('Invalid input, please try again.')