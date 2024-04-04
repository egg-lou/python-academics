operators = {
    '+': {'operation': lambda x, y: x + y, 'name': 'Addition'},
    '-': {'operation': lambda x, y: x - y, 'name': 'Subtraction'},
    '*': {'operation': lambda x, y: x * y, 'name': 'Multiplication'},
    '/': {'operation': lambda x, y: x / y, 'name': 'Division'}
}


def calculator(operation, num1, num2):
    if operation in operators:
        return operators[operation]['operation'](num1, num2)
    else:
        print('Invalid')
        return None


def print_operators(operations):
    for operation in operations:
        print(f"{operations[operator]['name']} {operation}")


if __name__ == '__main__':
    try:
        print_operators(operators)
        operator = input('Enter operator: ')
        if operator not in operators:
            raise ValueError()

        number1 = float(input(f'Enter first number: '))
        number2 = float(input(f'Enter second number: '))

        result = calculator(operator, number1, number2)

        print(f'{number1} {operator} {number2} =  {result}')

    except ValueError as e:
        print(f'Invalid input {e}')
