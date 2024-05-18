import random
import time


def math_quiz():
    random.seed(time.time())
    _num1 = random.randint(1, 100)
    _num2 = random.randint(1, 100)
    operators = ['+', '-', '*', '/']
    _operator = random.choice(operators)
    if _operator == '/':
        while _num2 == 0:
            _num2 = random.randint(1, 100)
    return _num1, _num2, _operator


def check_answer(_operator, _num1, _num2, _user_answer):
    answer = 0.0
    if _operator == '+':
        answer = _num1 + _num2
    elif _operator == '-':
        answer = _num1 - _num2
    elif _operator == '*':
        answer = _num1 * _num2
    elif _operator == '/':
        answer = round(_num1 / _num2, 2)
    return round(_user_answer, 2) == answer


if __name__ == '__main__':
    print("Welcome to Math Quiz")
    num1, num2, operator = math_quiz()

    max_tries = 3
    tries = 0

    while tries < max_tries:
        try:
            user_input = input(f"What is {num1} {operator} {num2}? \nAnswer: ")
            user_answer = float(user_input)
            if check_answer(operator, num1, num2, user_answer):
                if tries == 0:
                    print("YOU WON! You got it on the first try!")
                else:
                    print("YOU WON!")
                break
            else:
                print(f"Incorrect! You have {max_tries - tries - 1} tries left.")
                tries += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if tries == max_tries:
        print("Sorry, you've used all your tries. YOU LOSE!")
