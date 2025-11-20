import sys
import typing

def fibbinacii(ranking):
    ranking = typing.cast (int , ranking)
    i = 0;
    values = []
    values.append(0)
    i += 1
    values.append(1)
    i += 1
    while i <= ranking:
        values.append(values[i-1] + values[i-2])
        i += 1
    return values[ranking]

def fib_lookup(ranking):
    if not isinstance (ranking, int):
        raise TypeError("fib_lookup needs integer values")
    if not ranking in range(6):
        raise ValueError("fib_lookup only works for positive values up to 5")

    values = [0, 1, 1, 2, 3, 5]
    return values[ranking]


if __name__ == "__main__":
    print (fibbinacii(int(sys.argv[1])))
    print (fib_lookup(int(sys.argv[1])))
