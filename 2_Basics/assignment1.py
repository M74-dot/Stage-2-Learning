""" This python program makes use of variables, constants,
 operators, keywords and print statements"""

# declaring variables

number1 = int(input())
number2 = int(input())


# declaring constants

PI = 3.14


# Perform arithmetic operations

result1 = number1 + number2
result2 = number1 - number2
result3 = number1 * number2


# Print the results using different forms of print statements

print("The sum of number1 and number2 is: ", result1)
print(f"The difference between {number1} and {number2} is: {result2}")
print("The product of", number1, "and", number2, "is:", result3)


# use of different keywords

if result1 > result2:
    print('sum is greater than difference')
elif result1 < result2:
    print('difference is greater than sum')
else:
    print('Both are equal')


for i in range(0,11):
    print(i)

if 10 in list([1,2,3,4,5,6,7,8,9,10]):
    print('10 is present in list')
  