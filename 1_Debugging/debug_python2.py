class User:
    """A class docstring."""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        """Function printing name"""
        return self.name

    def get_email(self):
        """Function printing email"""
        return self.email

    def do_something(self):
        """Function printing user """
        pass

    def __str__(self):
        return self.name + ", " + self.email


users = [User('Manisha', 'manisha@gmail.com'),
         User('user2', 'user2@gmail.com')]

for i in users:
    i.do_something()
