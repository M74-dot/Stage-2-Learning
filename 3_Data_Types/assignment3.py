""" maximum number from 3 numbers """

# normal function

# def return_maximum(number1, number2, number3):
#     """ returns maximum number """
#     if number1 > number2 and number1 > number3:
#         print(number1)
#     elif number2 > number1 and number2 > number3:
#         print(number2)
#     else:
#         print(number3)

num1 = int(input())
num2 = int(input())
num3 = int(input())

# return_maximum(num1,num2,num3)


# Using Ternary operator

max_num = (num1 if (num1 > num2 and num1 > num3) else
     (num2 if (num2 > num1 and num2 > num3) else num3))

print(max_num)
 