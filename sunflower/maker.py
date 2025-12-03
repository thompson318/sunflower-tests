from time import sleep
from shutil import copyfile
from sunflower.fibonacci import fibonacci

# the delay is there to create the impression of 
# a more complex algorithm.
delay = 1

def make_sunflower(rank):
    print("Starting sunflower generation.")
    sleep(delay)
    print("Creating Fibonacci sequence.")
    fibonacci(rank)
    sleep(delay)
    print("Adding seeds.")
    sleep(delay)
    print("Creating petals.")
    sleep(delay)
    with open("sunflower/data/data.dat", "r") as filein:
        sunflower = filein.read()
    size = 64
    scale = 1
    if int(rank) > 0:
        size = size + 32 * int(rank)
        scale = scale + 0.5 * int(rank)
    sunflower = sunflower.replace("size", str(size))
    sunflower = sunflower.replace("myscale", str(scale))
    print("Sunflower complete.")
    return sunflower
