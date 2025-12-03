from time import sleep
import sys
import sunflower.maker


if __name__ == "__main__":
    rank = 0
    if len(sys.argv) > 1:
        rank = sys.argv[1]
    sunflower = sunflower.maker.make_sunflower(rank)
    with open("sunflower.svg", 'w') as file:
        file.write(sunflower)
    print("Output written to sunflower.svg")

    
