from time import sleep
from shutil import copyfile
from sunflower.fibonacci import fibonacci
from sunflower.drawer import draw

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
    sunflower = draw(rank)
    print("Sunflower complete.")
    return sunflower
