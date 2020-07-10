import arithmetics as x
import time

x.welcome()

time.sleep(5)

print("*" * 22)
print('Select Operator number')
print("*" * 22)

print('1. "+" for Addition')
print('2. "-" for Subtraction')
print('3. "*" for Multiplication')
print('4. "/" for Division')
print('5. "**" for Exponential')
print('6. "% "for modulus')


try:
    def calculate():
        time.sleep(5)

    while True:
        time.sleep(5)
        get_operator = input('please enter the arithmetic operator: ')
        if get_operator in ('1', '2', '3', '4', '5', '6'):
            num1 = int(input("Pls Enter first number: "))
            num2 = int(input("Pls Enter second number: "))

            if get_operator == '1':
                add = x.add(num1, num2)
                print(f"{num1} + {num2} = {add}")

            elif get_operator == '2':
                sub = x.subtract(num1, num2)
                print(f"{num1} - {num2} = {sub}")

            elif get_operator == '3':
                multiply = x.multiply(num1, num2)
                print(f"{num1} * {num2} = {multiply}")

            elif get_operator == '4':
                divide = x.divide(num1, num2)
                print(f"{num1} / {num2} = {divide}")

            elif get_operator == '5':
                expo = x.exponential(num1, num2)
                print(f"{num1} ** {num2} = {expo}")

            elif get_operator == '6':
                mod = x.modulus(num1, num2)
                print(f"{num1} % {num2} = {mod}")

            else:
                print("sorry enter integer value")


except ZeroDivisionError:
    print('pls enter anything apart from 0')
    x.repeat()

except ValueError as err:
    err = 'The value you entered is invalid, exiting....'
    print(err)
    x.repeat()

except KeyboardInterrupt as interrupt:
    interrupt = "User interrupt by pressing CTL + C"
    print(interrupt)
