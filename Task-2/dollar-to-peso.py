def convert_to_peso(value, rate):
    return value * rate


if __name__ == '__main__':
    try:
        peso_rate = 45.50
    
        amount = float(input('Input amount to convert: '))
        
        converted_amount = convert_to_peso(amount, peso_rate)
        
        print(f'${amount} is equal to Php {converted_amount}')
    
    except ValueError as e:
        print(f'Invalid Input {e}')
