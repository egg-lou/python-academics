def calculate_tax_interest(principal_amount):
    rate = 12 / 100
    time = 30 / 365
    tax_rate = 10 / 100

    interest = principal_amount * rate * time

    tax = interest * tax_rate
    
    net = interest - tax
    
    return tax, net


if __name__ == '__main__':
    try:
        principal = float(input('Enter your principal: '))

        withholding_tax, net_interest = calculate_tax_interest(principal)

        print(f'With holding tax: {withholding_tax:.2f}')
        
        print(f'Net Interest: {net_interest:.2f}')

    except ValueError as e:
        print(f'Invalid input {e}')
