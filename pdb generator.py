import RRCL
import pickle

colors = [0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5]

generation = 0
solved = {}
solved[tuple(colors)] = generation

newGen = [colors]

while generation < 5:
    lastgenList = []
    for item in newGen:
        lastgenList.append(item.copy())
    newGen = []
    generation += 1
    print(generation)
    print(len(lastgenList))
    for cube in lastgenList:
        for x in range(18):
            newCube = RRCL.rotateSide2x2(cube.copy(), x)
            tNewCube = tuple(newCube)
            if tNewCube not in solved:
                solved[tNewCube] = generation
                newGen.append(newCube)

# Save to a pickle file
with open("pdb.pkl", "wb") as f:
    pickle.dump(solved, f)
