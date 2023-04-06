def fib(num):
    """ Return the fibonacci series upto n. """
    fib_series = []
    a,b = 0,1
    while b < num+1:
        fib_series.append(b)
        a,b = b, a+b
    return fib_series
