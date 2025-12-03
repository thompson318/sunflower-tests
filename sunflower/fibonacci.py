import sys
import typing

def fibonacci(rank):
    rank = int(rank)
    
    values = [0,1]
    i = 2
    while rank > 1 and i <= rank:
        values.append(values[i-1] + values[i-2])
        i = i + 1
    return values[rank]
