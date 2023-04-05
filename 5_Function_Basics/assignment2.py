""" Function that takes list as input and returns 3 different lists """


def return_lists(obj1):
    
    object1 = obj1
    object2 = obj1.copy()
    object3 = []

    object2.append([len(obj1) + 1]*3)

    for i in range(len(object2)):
        object3.append([object2[i][j]*object2[i][j] if j==1 else object2[i][j] for j in range(3)])
    
    return object1,object2,object3


no_of_elements = int(input())
size_of_sublist = int(input())

obj1 = [[int(input())
            for j in range(size_of_sublist)] for i in range(no_of_elements)]

lst1, lst2, lst3 = return_lists(obj1)

print("Object1 = ", lst1)
print("Object2 = ", lst2)
print("Object3 = ", lst3)
