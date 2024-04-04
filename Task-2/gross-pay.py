def calculate_gross_pay(rate, hours):
    return rate * hours


if __name__ == '__main__':
    try:
        rate_per_hour = 84.50

        working_hours = float(input("How many work hours: "))

        gross_pay = calculate_gross_pay(rate_per_hour, working_hours)

        print(f'{working_hours} hours worked is equal to Php{gross_pay}')

    except ValueError as e:

        print(f'Please enter a number {e}')
