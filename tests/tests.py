from mypackage import recursion
from mypackage import sorting

def bubble_sort():
    """
    make sure bubble_sort works correctly
    """

    assert myFunction.bubble_sort([2, 5, 7, 3, 9, 8, 6, 5, 1, 0]) == [0, 1, 2, 3, 5, 5, 6, 7, 8, 9], 'incorrect'
    assert myFunction.bubble_sort([2, 5, 59, 8, 16, 54, 1, 0]) == [0, 1, 2, 5, 8, 16, 54, 59], 'incorrect'
    assert myFunction.bubble_sort([2, 5, 0]) == [0, 2, 5], 'incorrect'

def merge_sort():
    '''
    Make sure Merge_sort works correctly
    '''

    assert myFunction.merge_sort([5,32, 44, 66, 13, 76, 51, 23]) == [[5, 13, 23, 32, 44, 51, 66, 76]], 'incorrect'
    assert myFunction.merge_sort([5,32, 0, 76, 51, 23]) == [[0, 5, 23, 32, 51, 76]], 'incorrect'
    assert myFunction.bubble_sort([3, 0, 76, 51, 4]) == [[0, 3, 4, 51, 76]], 'incorrect'

def sum_array():
    '''
    Make sure sum_array works correctly
    '''
    assert myFunction.sum_array([2, 6, 4, 5]) == 17, 'incorrect'
    assert myFunction.sum_array([2, 6, 4, 5, 16]) == 33, 'incorrect'
    assert myFunction.sum_array([22, 6, 14, 9, 16]) == 67, 'incorrect'


def fibonacci():
    '''
    Make sure fibonacci works correctly
    '''
    assert myFunction.fibonacci(8) == 13, 'incorrect'
    assert myFunction.fibonacci(19) == 2584, 'incorrect'
    assert myFunction.fibonacci(1) == 0, 'incorrect'
    assert myFunction.fibonacci(2) == 1, 'incorrect'


def factorial():
    '''
    Make sure factorial works correctly
    '''
    assert myFunction.factorial(5) == 120, 'incorrect'
    assert myFunction.factorial(8) == 40320, 'incorrect'
    assert myFunction.factorial(0) == 1, 'incorrect'


def reverse():
    '''
    Make sure reverse works correctly
    '''
    assert myFunction.reverse('hello') == 'olleh', 'incorrect'
    assert myFunction.reverse('incorrect') == 'tcerrocni', 'incorrect'
    assert myFunction.reverse('myFunction') == 'tcerrocnim', 'incorrect'
