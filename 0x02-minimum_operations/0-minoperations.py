#!/usr/bin/python3
"""
Main file task
"""


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """

    op = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            op += factor
            n = n / factor
        factor += 1

    return op
