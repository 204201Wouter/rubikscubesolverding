import RRCL
import pickle

colors = [0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5]

# BFS initialization
generation = 0
solved = {tuple(colors): generation}
newGen = [colors]
i = 0

while generation < 8:
    print(f'Generation: {generation}, New States: {len(newGen)}, Total Solved: {len(solved)}')
    
    nextGen = []
    generation += 1

    for cube in newGen:
        for x in range(18):
            rotated = RRCL.rotateSide2x2(cube, x)
            cube_key = tuple(rotated)
            if cube_key not in solved:
                i += 1
                solved[cube_key] = generation
                nextGen.append(rotated)
                if i % 10000 == 0:
                    print(f'{i} new states')

    newGen = nextGen

# Save result
with open("pdb.pkl", "wb") as f:
    pickle.dump(solved, f)
