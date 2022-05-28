"""
Fibonacci factorial
"""

import timeit

def factorial_recursive(nnumb):
    """
    Returns factorial recursively
    >>> factorial_recursive(10)
    3628800
    """
    if nnumb == 1:
        return 1
    else:
        return nnumb * factorial_recursive(nnumb - 1)
def factorial_iterative(nnumm):
    """
    Returns factorial iteratively
    >>> factorial_iterative(10)
    3628800
    """
    if nnumm == 0:
        res = 0
    else:
        res = 1
        for koee in range(1, nnumm + 1):
            res *= koee
    return res
def fibonacci_recursive(nnuum):
    """
    Returns fibonacci recursively
    >>> fibonacci_recursive(15)
    987
    """
    if nnuum <= 1:
        return 1
    else:
        return fibonacci_recursive(nnuum - 1) + fibonacci_recursive(nnuum - 2)
def fibonacci_iterative(numbb):
    """
    Returns fibonacci iteratively
    >>> fibonacci_iterative(15)
    987
    """
    if numbb < 2:
        return numbb
    ollo, koe = 1, 1
    while numbb > 1:
        koe2 = koe
        koe = ollo + koe
        ollo = koe2
        numbb -= 1
    return koe

def time_factrec():
    """
    Returns the duration of recursive factorial
    >>> ":-)" != ":-("
    True
    """
    starttime = timeit.default_timer()
    factorial_recursive(100)
    return timeit.default_timer() - starttime

def time_factiter():
    """
    Returns the duration of iterative factorial
    >>> ":-)" != ":-("
    True
    """
    starttime = timeit.default_timer()
    factorial_iterative(100)
    return timeit.default_timer() - starttime

def time_fibonrec():
    """
    Returns the duration of recursive fibonacci
    >>> ":-)" != ":-("
    True
    """
    starttime = timeit.default_timer()
    fibonacci_recursive(37)
    return timeit.default_timer() - starttime

def time_fiboiter():
    """
    Returns the duration of iterative fibonacci
    >>> ":-)" != ":-("
    True
    """
    starttime = timeit.default_timer()
    fibonacci_iterative(37)
    return timeit.default_timer() - starttime


def numbers_time_test(function=0, realisation=0, verbose=False):
    """
    Defines from which function return time
    >>> ":-)" != ":-("
    True
    """
    if verbose==True:
        if function == 0:
            if realisation == 0:
                return time_factrec()
            else:
                return time_factiter()
        else:
            if realisation == 0:
                return time_fibonrec()
            else:
                return time_fiboiter()
