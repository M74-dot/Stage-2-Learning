class ListOperations:
    def __init__(self, new_list):
        self.list1 = new_list

    def append_element(self, element):
        self.list1.append(element)
        print(f"{element} is added to list")

    def delete_element(self, index):
        self.list1.pop(index)
        print(f"element at index {index} is popped")

    def display_list(self):
        print('List elements are: ')
        for element in self.list1:
            print(element)


list1 = ListOperations([0, 2, 4])
list1.append_element(6)
list1.append_element(8)
list1.display_list()
list1.delete_element(1)
list1.display_list()
