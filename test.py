import RRCL
from random import randint
with open("pdb.txt") as outfile:
    pdb = eval(outfile.read())
    #pdb = outfile.read()
print('loaded')

cube = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']

for x in range(2):
    cube = RRCL.rotateSide(cube, randint(0,5))


for item in range(len(cube)):
    if cube[item] == 'white':
        cube[item] = 0
    if cube[item] == 'yellow':
        cube[item] = 1
    if cube[item] == 'green':
        cube[item] = 2
    if cube[item] == 'blue':
        cube[item] = 3
    if cube[item] == 'red':
        cube[item] = 4
    if cube[item] == 'orange':
        cube[item] = 5

corners = (cube[0], cube[2], cube[6], cube[8], cube[9], cube[11], cube[15], cube[17], cube[18], cube[20], cube[24], cube[26], cube[27], cube[29], cube[33], cube[35], cube[36], cube[38], cube[42], cube[44], cube[45], cube[47], cube[51], cube[53])


print(corners)
print(pdb[tuple(corners)])