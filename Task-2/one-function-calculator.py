
if __name__ == '__main__':
    try:
        number1 = int(input('First number: '))
        number2 = int(input('Second number: '))

        result = lambda num1, num2: num1 + num2

        print(f'{number1} + {number2} = {result(number1, number2)}')

    except ValueError as e:
        print(f'Invalid input {e}')
