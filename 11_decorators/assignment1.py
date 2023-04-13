import time


class Timer:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {self.func.__name__} is: {end_time-start_time:.2f} seconds")
        return result


@Timer
def function(number1, number2):
    # lst = [1] * 100000
    # print(lst)
    print('Hey There.!')
    print(f"Product is: {number1 * number2}")
    
function(1000,2332)