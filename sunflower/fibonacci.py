import sys
import typing

def fibonacci(rank):
    rank = int(rank)
    if not rank in range(6):
        raise ValueError("fibonacci only works for positive values up to 5")

    values = [0, 1, 1, 2, 3, 5]
    return values[rank]
