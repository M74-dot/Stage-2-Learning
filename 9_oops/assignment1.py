class DisplayString:
    """ class to print user input """

    def __init__(self):
        self.name = input('Enter your name: ')

    def print_string(self):
        print(f"User name is: {self.name}")


user1 = DisplayString()
user1.print_string()

user2 = DisplayString()
user2.print_string()
