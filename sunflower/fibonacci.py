import sys
import typing

def fibonacci(rank):
    if not isinstance (rank, int):
        raise TypeError("fibonacci needs integer values")
    if not rank in range(6):
        raise ValueError("fibonacci only works for positive values up to 5")

    values = [0, 1, 1, 2, 3, 5]
    return values[rank]
