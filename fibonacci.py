import sys

def fibbinacii(ranking):
    i = 0;
    values = []
    values.append(0)
    values.append(1)
    i = 1
    while i <= ranking:
        values.append(values[i] + values[1-1])
        i += 1
    print (values)
    return values[ranking]


if __name__ == "__main__":
    print (fibbinacii(int(sys.argv[1])))
