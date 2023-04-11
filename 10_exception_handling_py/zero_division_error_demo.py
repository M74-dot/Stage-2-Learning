""" ZeroDivisionError demo """

try:
    number1 = float(input('Enter numerator: '))
    number2 = float(input('Enter denominator: '))
    print(f" Division is: {number1/number2:.2f}")

except ZeroDivisionError:
    # print(ZeroDivisionError)
    print("Can't divide by zero")

else:
    print('Executed Successfully..')
