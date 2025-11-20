from time import sleep
from shutil import copyfile
import sunflower.maker

if __name__ == "__main__":
    sunflower = sunflower.maker.make_sunflower()
    with open("sunflower.svg", 'w') as file:
        file.write(sunflower)
    print("Output written to sunflower.svg")

    
