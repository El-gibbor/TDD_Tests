#!/usr/bin/python3
"""
    A module that sums to int or foat values
    and  Returns Sum of the two arguments

"""


def add_integer(a, b=98):
    """ Return the sum of two integers or floats as integers
    Args:
        a - (int/float): first argument
        b - (int/float): second argument
    Raises:
        TypeError: If either of the args is not an integer or float
    """
    if not isinistance(a, (int, float)):
        raise Exception('a must be an integer')
    if not isinistance(b, (int, float)):
        raise Exception('b must be an integer')
    return int(a) + int(b)
