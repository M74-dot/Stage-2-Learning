""" TypeError demo """


def multiply_numbers(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both arguments must be numbers")
    product = x * y
    return product


num1 = 5
num2 = "10"

result = multiply_numbers(num1, num2)

print(result)
