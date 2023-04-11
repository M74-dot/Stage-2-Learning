""" IndexError demo """

my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[6])
except IndexError:
    print("Index out of range")
