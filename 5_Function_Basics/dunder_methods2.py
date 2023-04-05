import os

class DunderMethods:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self,other):
        return self.value == other.value
    
    def __str__(self):
        return f"{self.value}"
    
    def __repr__(self):
        return f"DunderMethods('{self.value}')"
    
    def __len__(self):
        return len(str(self.value))
    

if __name__ == "__main__":

    a = DunderMethods(10)
    b = DunderMethods(20)

    print(a<b)
    print(a == b)
    print(str(a))
    print(repr(a))
    print(len(a))
