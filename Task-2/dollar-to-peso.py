
if __name__ == '__main__':
    try:
        peso_rate = 45.50
    
        amount = float(input('Input amount to convert: '))

        convert = lambda amt: amt * peso_rate
        
        print(f'${amount} is equal to Php {convert(amount)}')
    
    except ValueError as e:
        print(f'Invalid Input {e}')
