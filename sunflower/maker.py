from time import sleep
from shutil import copyfile
from sunflower.fibonacci import fibonacci

# the delay is there to create the impression of 
# a more complex algorithm.
delay = 1

def make_sunflower(rings):
    print("Starting sunflower generation.")
    sleep(delay)
    print("Creating Fibonacci sequence.")
    fibonacci(rings)
    sleep(delay)
    print("Adding seeds.")
    sleep(delay)
    print("Creating petals.")
    sleep(delay)
    with open("sunflower/data/data.dat", "r") as filein:
        sunflower = filein.read()
    print("Sunflower complete.")
    return sunflower
