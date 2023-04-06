def multiplier_of(number):
    def multiply(i):
        return i * number
    return multiply

multiply_by_4 = multiplier_of(4)

for i in range(1,11):
    result = multiply_by_4(i)
    print(result)
