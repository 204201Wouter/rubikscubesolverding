import RRCL
import random
import pickle
import pygame



def scrambleCube():
    global cube
    for _ in range(20):
        cube = RRCL.rotateSide(cube, random.randint(0,17))





def getNeighbors(colors):
    neigbors = []
    for x in range(6):
        for y in range(3):
            currentCube = colors
            for _ in range(y + 1):
                currentCube = RRCL.rotateSide(currentCube, x)
            neigbors.append([currentCube, x + y*6])
    
    return neigbors



def hCost(cube):



    corners = (cube[0], cube[2], cube[6], cube[8], cube[9], cube[11], cube[15], cube[17], cube[18], cube[20], cube[24], cube[26], cube[27], cube[29], cube[33], cube[35], cube[36], cube[38], cube[42], cube[44], cube[45], cube[47], cube[51], cube[53])

    if tuple(corners) in pdb:
       # print(pdb[tuple(corners)])
        return pdb[tuple(corners)]
    else:
        return 20
    


def getNeighbours(cube, openSet):
    neighbours = []
    for x in range(18):


        neighbour = RRCL.rotateSide(cube, x)

        turns = openSet[tuple(cube)]["turns"].copy()
        turns.append(x)
        neighbours.append([tuple(neighbour), {"hCost": hCost(neighbour), "turns": turns}])

     #   discovoredCubes[tuple(rotate)] = {"hCost": hCost(rotate), "turns": turns}

   # print(neighbours)
    return neighbours



def lowestFvalue(discoveredCubes):
    return min(discoveredCubes, key=lambda k: discoveredCubes[k]['hCost'] + len(discoveredCubes[k]['turns']))
    key = random.choice(list(discoveredCubes.keys()))
    return key




def AStar(colorsList):

    openSet = {}
    openSet[tuple(colorsList)] = {"hCost": hCost(colorsList), "turns": []}
    closedSet = {}

    while len(openSet) > 0:

        cube = lowestFvalue(openSet)
       # print(openSet[cube]["hCost"])
        

        if cube == tuple(solvedCube):
            return openSet[cube]

        closedSet[cube] = {"hCost": openSet[cube]["hCost"], "turns": openSet[cube]["turns"]}
        

        neighbours = getNeighbours(list(cube), openSet)
        for neighbour in neighbours:

            if not neighbour[0] in closedSet:
                if neighbour[0] in openSet:
  
                    if neighbour[1]["hCost"]+len(neighbour[1]["turns"]) < openSet[neighbour[0]]["hCost"]+len(openSet[neighbour[0]]["turns"]) :
                        openSet[neighbour[0]]["hCost"] = neighbour[1]["hCost"]
                        openSet[neighbour[0]]["turns"] = neighbour[1]["turns"]


                else:
                    openSet[neighbour[0]] = neighbour[1]

        openSet.pop(cube)
      
    





    '''

    discoveredCubes = {}
    discoveredCubes[tuple(colorsList)] = {"hCost": hCost(colorsList), "turns": []}




    while not tuple(solvedCube) in discoveredCubes:
       # a = discoveredCubes[lowestFvalue(discoveredCubes)]
        #print(a["hCost"] + len(a["turns"]))



        discoveredCubes = discoverNewCubes(list(lowestFvalue(discoveredCubes)), discoveredCubes)



    

    return discoveredCubes[tuple(solvedCube)]["turns"]
    '''

with open("pdb.pkl", "rb") as f:
    pdb = pickle.load(f)

print('loaded pdb')

solvedCube = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
solvedCube = [0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5]

cube = solvedCube.copy()
# cube = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 4, 0, 5, 4, 4, 3, 2, 4, 5, 5, 4, 4, 3, 5, 2, 3, 2, 4, 5, 5, 3, 3, 3, 1, 4, 4, 2, 2, 2, 2, 2, 2, 5, 5, 5, 3, 3, 3]


#scrambleCube()
#'''
for x in range(6):
    cube = RRCL.rotateSide(cube, random.randint(0,17))


#'''

print(cube)
cubeBegin = cube.copy()
#cube = RRCL.rotateSide(cube, random.randint(0,17))


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




solved = AStar(cube)

turns = solved["turns"]
print(turns)

step = 0





pygame.init()


screen = pygame.display.set_mode((800,600))
screenSize = screen.get_size()

screenCenter = [screenSize[0]/2, screenSize[1]/2]

colors = cubeBegin

angle = [0,0]

while True:
    mouse = False
    for event in pygame.event.get():     
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print(colors)
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True

        if event.type == pygame.KEYDOWN:
            colors = RRCL.rotateSide(colors, turns[step]) 

            step += 1
            

                          
    screen.fill((0,0,0))


    




    angle = RRCL.detectRotations(pygame.mouse.get_pressed(), pygame.mouse.get_rel() ,angle)




    colors = RRCL.renderCube(colors, angle, screen, mouse, pygame.mouse.get_pos(), True)
   

    pygame.display.update()


    