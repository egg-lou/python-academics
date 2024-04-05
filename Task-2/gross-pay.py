
if __name__ == '__main__':
    try:
        rate_per_hour = 84.50

        working_hours = float(input("How many work hours: "))

        gross_pay = lambda working_hours: working_hours * rate_per_hour

        print(f'{working_hours} hours worked is equal to Php{gross_pay(working_hours)}')

    except ValueError as e:
        print(f'Please enter a number {e}')
