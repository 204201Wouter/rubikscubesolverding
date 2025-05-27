import RRCL
import random
import pickle

solvedCube = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']


cube = solvedCube.copy()

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



def hCost(cube, pdb):
   # krijg hwaarde uit pdb
    cube = tuple(cube)
    if cube in pdb:
        return pdb[cube]
    else:
        return 20

def AStar(colorsList):

    with open("pdb.pkl", "rb") as f:
        pdb = pickle.load(f)
        

    colors = tuple(colorsList)

    openSet = []
    fScores = {}
    gScores = {}
    turnUsed = {}

    openSet.append(colors)
    gScores[colors] = 0
    fScores[colors] = hCost(colors, pdb)

    while len(openSet) > 0:
        bestCube = tuple(solvedCube)
        bestScore = float('inf')
        for cube in openSet:
            if fScores[tuple(cube)] < bestScore:
                bestCube = cube
                bestScore = fScores[cube]
        
        if bestCube == tuple(solvedCube):
            path = []

            current = bestCube
            path.append(turnUsed[current][1])
            while current in turnUsed:
                current = turnUsed[current][0]
                path.append(turnUsed[current][1])

            print("gelukt")
            return path
        
        openSet.remove(bestCube)
        neigbors = getNeighbors(list(bestCube))
        for neighbor in neigbors:
            tentGScore = gScores[bestCube] + 1
            neighbor[0] = tuple(neighbor[0])
            if (not neighbor[0] in gScores) or tentGScore < gScores[neighbor[0]]:
                turnUsed[neighbor[0]] = neighbor
                gScores[neighbor[0]] = tentGScore
                fScores[neighbor[0]] = tentGScore + hCost(neighbor[0],pdb)
                if not neighbor[0] in openSet:
                    openSet.append(neighbor)
    
    print("mislukt")
    return []


#scrambleCube()
cube = RRCL.rotateSide(cube, random.randint(0,17))

print(AStar(cube))

