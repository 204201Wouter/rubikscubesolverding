import RRCL
import pickle



colors = [0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5]


generation = 0
solved = {tuple(colors): generation}
newGen = [colors]
i = 0

while len(newGen) > 0:
    
    
    nextGen = []
    generation += 1

    for cube in newGen:
        for x in range(18):
            rotated = RRCL.rotateSide2x2(cube, x)
            cube_key = tuple(rotated)
            i += 1
            if i % 1000000 == 0:
                with open("pdb.pkl", "wb") as f:
                    pickle.dump(solved, f)
                print(f'Saved and Solved: {len(solved)} Generation: {generation}, lastGen: {len(newGen)}')
  

            if cube_key not in solved:
                
                solved[cube_key] = generation
                nextGen.append(rotated)
           

    newGen = nextGen

# Save result
with open("pdb.pkl", "wb") as f:
    pickle.dump(solved, f)
