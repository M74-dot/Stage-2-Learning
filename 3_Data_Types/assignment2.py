# Input : [[1,1,1],[2,2,2],[3,3,3]]
# Output
# Obj1 = [[1,1,1],[2,2,2],[3,3,3]]
# Obj2 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

import copy


no_of_elements = int(input())
size_of_sublist = int(input())

object1 = [[int(input())
            for j in range(size_of_sublist)] for i in range(no_of_elements)]

object2 = copy.deepcopy(object1)
object2.append([4,4,4])

print(object1)
print(object2)
