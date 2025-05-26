from collections import deque


class Corners:
    def __init__(self, corners=None):
        if corners != None:
            self.corners = corners
        else:
            self.corners = [(i, 0) for i in range(8)]

    def isSolved(self):
        return all(pos == i and rot == 0 for i, (pos, rot) in enumerate(self.corners))
    
    def copy(self):
        return Corners(self.corners.copy())
    
    def rotateSide(self, side):
        moveTable = {
            'U':  [(0,1), (1,2), (2,3), (3,0)],
            'R':  [(0,4), (4,5), (5,1), (1,0)],
            'F':  [(0,3), (3,7), (7,4), (4,0)],
        }

        orientationChange = {
            'U': [0, 0, 0, 0],
            'R': [2, 1, 2, 1],
            'F': [1, 2, 1, 2],
        }

        newCorners = self.corners.copy()

        for i in range(4):
            corner = self.corners[moveTable[side][i][0]]
            rot = (corner[1] + orientationChange[side][i]) % 3
            newCorners[moveTable[side][i][1]] = (corner[0], rot)

        self.corners = newCorners
    
cornerMap = {
    tuple(sorted(("white", "green", "red"))) : 0,
    tuple(sorted(("white", "green", "orange"))) : 3,
    tuple(sorted(("white", "blue", "red"))) : 1,
    tuple(sorted(("white", "blue", "orange"))) : 2,
    tuple(sorted(("yellow", "green", "red"))) : 5,
    tuple(sorted(("yellow", "green", "orange"))) : 4,
    tuple(sorted(("yellow", "blue", "red"))) : 6,
    tuple(sorted(("yellow", "blue", "orange"))) : 7
}

def piecesToNumbers(corners):
    numbers = Corners()
    for key, value in corners.items():
        pos = cornerMap[sorted(key)]
        index = cornerMap[sorted(value)]
        rot = 0 # niet af

        numbers.corners[index] = (pos, rot)

def generateCornersPDB():
    solved = Corners()
    visited = {}
    queue = deque([(solved, 0)])

    while queue:
        cube, depth = queue.popleft()
        key = tuple(cube.corners)

        if key in visited or depth > 11:
            continue

        visited[key] = depth

        if len(visited) % 1000 == 0:
            print(len(visited))


        for move in ['U', 'R', 'F']:
            for x in range(1, 4):  # 90, 180, 270 degree turns
                nextCube = cube.copy()
                for _ in range(x):
                    nextCube.rotateSide(move)
                queue.append((nextCube, depth + 1))



    return visited

pdb = generateCornersPDB()

print(pdb)

with open("data.txt", "w") as outfile:
    outfile.write(str(pdb))

print(len(pdb))
#print(pdb)