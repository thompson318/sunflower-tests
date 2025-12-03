
def draw (rank):
    with open("sunflower/data/data.dat", "r") as filein:
        sunflower = filein.read()
    size = 64
    scale = 1
    if int(rank) > 0:
        size = size + 32 * int(rank)
        scale = scale + 0.5 * int(rank)
    sunflower = sunflower.replace("size", str(size))
    sunflower = sunflower.replace("myscale", str(scale))
    return sunflower
