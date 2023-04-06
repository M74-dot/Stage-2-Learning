""" Creating an iterator """


class NumberIterator:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 10:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration


iterator = NumberIterator()

for number in iterator:
    print(number)
