""" demonstration of agruments """


def display_argument_type(required_args, default_args="hey its default value", *args, **kwargs):

    print('Required argument: ', required_args)

    print('Default argument: ', default_args)

    if args:
        print('Variablr length arguments: ')
        for argument in args:
            print(argument)

    if kwargs:
        print('Keyword arguments: ')
        for key, value in kwargs.items():
            print(key, ' -> ', value)


def line_break():
    print('\n')

# Testing the function


# Positional or required
display_argument_type('Hello Python')
line_break()

# default
display_argument_type('Hello World.!', 'Replacement of default value')
line_break()

# variable length args
display_argument_type('Hey Manisha.!', 'argument1',
                      'argument2', 'argument3', 'argument4')
line_break()

# keyword arguments
display_argument_type('Hey its required argument',
                      name='Sweety', age='22', college='WCE')
line_break()
