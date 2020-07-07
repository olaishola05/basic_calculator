# this file is my module for all arithmetic operations


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def modulus(a, b):
    return a % b


def exponential(a, b):
    return a ** b


def repeat():
    new_cal = input(''' Do you want to perform  another calculation?\n Please enter Y for YES and N for NO: ''')
    if new_cal.upper() == 'Y':
        from calc import calculate
        calculate()

    elif new_cal.upper() == 'N':
        print('Thanks and see u later ')

    else:
        repeat()


def welcome():
    print("*" * 27)
    print('Welcome to basic calculator')
    print("*" * 27)
