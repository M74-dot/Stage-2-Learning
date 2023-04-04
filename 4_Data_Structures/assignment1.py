""" List comprehension and Dict  comprehension"""


numbers = [1,2,3,4,5]

# using list comprehension to create list of tuple
square_list = [(i,i**2) for i in numbers]


# using dict comprehension to create dict
square_dict = {key : value for (key,value) in square_list}

print(square_list)
print(square_dict)
