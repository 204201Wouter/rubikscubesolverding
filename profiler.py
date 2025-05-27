import time
import RRCL
import random


def functie():
    colors = [0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5]
    for x in range(1000000):
        RRCL.rotateSide2x2(colors, 0)


lijst = {}
for x in range(1000000):
    lijst[random.random()] = 1

def functie2():
    for x in range(1000000):
        y = 0.13895 in lijst
    return y

startTime = time.time()
functie()
print(f"Time: {time.time() - startTime} s")