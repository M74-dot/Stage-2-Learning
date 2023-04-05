import os


class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"{self.name},{self.age},{self.salary}"
    
    def __repr__(self):
        return f"Employee('{self.name},{self.age},{self.salary}')"
    
    def __eq__(self, other_employee):
        if isinstance(other_employee, Employee):
            return self.name == other_employee.name and self.age == other_employee.age and self.salary == other_employee.salary
        return False
    
    def __lt__(self,other_employee):
        if isinstance(other_employee, Employee):
            return self.salary < other_employee.salary
        return NotImplemented
    

# Execution point
if __name__ == '__main__':

    Manisha = Employee('Manisha Mali', 22, 30000)
    Shivkanya = Employee('Shivkanya Gore', 26, 33000)
    Sawat = Employee('Sawat Mali', 24, 10000)

    # __str__ method returns string rep of the object
    print(Manisha)

    # __repr__ method 
    print(repr(Shivkanya))

    # __eq__ method return equality between objects
    print(Manisha == Sawat)

    # __lt__ defines how to compare two objects
    print(Manisha < Shivkanya)

    # __dir__ returns list of methods of the objects
    print(dir(Sawat))

    # __file__ returns full path of the current file
    print(__file__)
