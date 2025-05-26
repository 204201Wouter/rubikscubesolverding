import RRCL

colors = [0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5]



generation = 0
with open("pdb.txt", "w") as f:
    content = '{'+f"{tuple(colors)}:{generation},\n"
    f.write(content)



solved = set()
solved.add(tuple(colors))

newGen = [colors]
with open("pdb.txt", "a") as f:
        
    while generation < 10:
        lastgenList = []
        for item in newGen:
            lastgenList.append(item.copy())
       # print(lastgenList)
        newGen = []
        generation += 1
        print(generation)
        for cube in lastgenList:
            for x in range(6):
                newCube = RRCL.rotateSide2x2(cube.copy(), x)
                tNewCube = tuple(newCube)
                if not tNewCube in solved:
                    content = f"{tNewCube}:{generation},\n"
                    f.write(content)
                    newGen.append(newCube)
                    solved.add(tNewCube)
    



    content = "}"
    f.write(content)

#print(solved)



