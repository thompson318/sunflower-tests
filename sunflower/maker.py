from time import sleep
from shutil import copyfile
import sunflower.fibonacci

delay = 0

def make_sunflower():
    print("Starting sunflower generation.")
    sleep(delay)
    print("Creating Fibonacci sequence.")
    sleep(delay)
    print("Adding seeds.")
    sleep(delay)
    print("Creating petals.")
    sleep(delay)
    with open("sunflower/data/data.dat", "r") as filein:
        sunflower = filein.read()
    return sunflower
    print("Sunflower complete.")
