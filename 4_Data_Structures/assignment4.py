""" generator expression to find sum of cube of first 20 natursl numbers """

n = 20

sum_of_cube = sum(i**3 for i in range(1, n+1))

print(sum_of_cube)
