
if __name__ == '__main__':
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Must be a number.")

    print(f"{num} is an {'Even Number' if num % 2 == 0 else 'Odd Number'}")