import RRCL
import random

solvedCube = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']


cube = solvedCube

def scrambleCube():
    global cube
    for _ in range(20):
        r = random.randint(0,17)
        cube = RRCL.rotateSide(cube, r)

edgeMap = {
        ("white", "green") : [7, 19],
        ("white", "blue") : [1, 34],
        ("white", "red") : [5, 37],
        ("white", "orange") : [3, 46],
        ("yellow", "green") : [10, 25],
        ("yellow", "blue") : [16, 28],
        ("yellow", "red") : [14, 43],
        ("yellow", "orange") : [12, 52],
        ("green", "red") : [23, 39],
        ("green", "orange") : [21, 50],
        ("blue", "red") : [32, 41],
        ("blue", "orange") : [30, 48]
}

cornerMap = {
        ("white", "green", "red") : [8, 20, 36],
        ("white", "green", "orange") : [6, 18, 47],
        ("white", "blue", "red") : [2, 35, 38],
        ("white", "blue", "orange") : [0, 33, 45],
        ("yellow", "green", "red") : [11, 26, 42],
        ("yellow", "green", "orange") : [9, 24, 53],
        ("yellow", "blue", "red") : [17, 29, 44],
        ("yellow", "blue", "orange") : [15, 27, 51]
}

def colorsToPieces(colors): # convert colors to pieces
    cMap = cornerMap("white", "green", "red")
    cornerWGR = tuple(sorted(colors[cMap[0]],colors[cMap[1]],colors[cMap[2]]))


    edges = {}
    for key, value in edgeMap.items():
        edges[key] = [colors[value[0]], colors[value[1]]]
    
    corners = {}
    for key, value in cornerMap.items():
        corners[key] = [colors[value[0]], colors[value[1]], colors[value[2]]]

    return [edges, corners]

def piecesToColors(edges, corners):
    colors = solvedCube
        
    for key, value in edges.items():
        indices = edgeMap[key]
        colors[indices[0]] = value[0]
        colors[indices[1]] = value[1]

    for key, value in corners.items():
        indices = cornerMap[key]
        colors[indices[0]] = value[0]
        colors[indices[1]] = value[1]
        colors[indices[2]] = value[2]

    return colors

scrambleCube()

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

    with open("pdb.txt") as outfile:
        pdb = eval(outfile.read())
        

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
        
        if bestCube == solvedCube:
            path = []

            current = bestCube
            path.append(turnUsed[current][1])
            while current in turnUsed:
                current = turnUsed[current][0]
                path.append(turnUsed[current][1])

            return path
        
        openSet.remove(bestCube)
        neigbors = getNeighbors(list(bestCube))
        for neighbor in neigbors:
            tentGScore = gScores[bestCube] + 1
            neighbor[0] = tuple(neighbor[0])
            if not neighbor[0] in gScores or tentGScore < gScores[neighbor[0]]:
                turnUsed[neighbor[0]] = neighbor
                gScores[neighbor[0]] = tentGScore
                fScores[neighbor[0]] = tentGScore + hCost(neighbor[0],pdb)
                if not neighbor[0] in openSet:
                    openSet.append(neighbor)
    
    print("mislukt")
    return []


AStar(tuple(cube))

