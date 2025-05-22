import pygame
import math
from sys import exit
import random
import numpy as np
import RRCL
from random import randint


pygame.init()


screen = pygame.display.set_mode((800,600))
screenSize = screen.get_size()

screenCenter = [screenSize[0]/2, screenSize[1]/2]







edgePieces = { 
    1: 34,
    3: 46,
    5: 37,
    7: 19,

    10: 25,
    12: 52,
    14: 43,
    16: 28,

    19: 7,
    21: 50,
    23: 39,
    25: 10,

    28: 16,
    30: 48,
    32: 41,
    34: 1,

    37: 5,
    39: 23,
    41: 32,
    43: 14,

    46: 3,
    48: 30,
    50: 21,
    52: 12,


}





cornerPieces = {
    0: [33, 45],
    2: [35, 38],
    6: [18, 47],
    8: [20, 36],

    9: [24, 53],
    11: [26, 42],
    15: [27, 51],
    17: [29, 44],

    18: [6, 47],
    20: [8, 36],
    24: [9, 53],
    26: [11, 42],

    27: [15, 51],
    29: [17, 44],
    33: [0, 45],
    35: [2, 38],

    36: [8, 20],
    38: [2, 35],
    42: [11, 26],
    44: [17, 29],


    45: [0, 33],
    47: [6, 18],
    51: [15, 27],
    53: [9, 24]   


}

def whiteAbove(center):

    if center == 22:
        return colors[edgePieces[19]] == 'white'
    if center == 31:
        return colors[edgePieces[34]] == 'white'
    if center == 40:
        return colors[edgePieces[37]] == 'white'
    if center == 49:
        return colors[edgePieces[46]] == 'white'
    





def currentEdgeWorkingOn():

  
       
    lastI = -1
    edges = []

    for x in range(4):
        while True:
            i = colors.index('white', lastI+1)
            lastI = i
            if i in edgePieces:
                edges.append(i)
                break


    notCorrectEdges = []
    notTopEdges = []


    
    for edge in edges:
        if not (colors[edgePieces[edge]] == colors[(edgePieces[edge]//9)*9+4]):
            notCorrectEdges.append(edge)
        if edge >= 9:
            notTopEdges.append(edge)


    return [notCorrectEdges, notTopEdges]





def whiteCrossA():
    global step
    global colors


       
    lastI = -1
    edges = []

    for x in range(4):
        while True:
            i = colors.index('white', lastI+1)
            lastI = i
            if i in edgePieces:
                edges.append(i)
                break
    
    
    notCorrectEdges = []
    
    for edge in edges:
       # if (colors[edgePieces[edge]] == colors[edgePieces[edge]//6*6+4] and edge < 9): # if not goede plek
        if not (edge < 9):
            notCorrectEdges.append(edge)


    
    if len(notCorrectEdges) > 0:
        edge = notCorrectEdges[random.randint(0,len(notCorrectEdges)-1)] # random om alle edges op een vlak error te voorkomen
       # print(whiteAbove((edgePieces[edge]//9)*9+4))
       # print((edgePieces[edge]//9)*9+4)
        if whiteAbove((edgePieces[edge]//9)*9+4):
            colors = RRCL.rotateSide(colors, 0)
           # print('wit boven')
        else:


            if edgePieces[edge]//9 == 0 or edgePieces[edge]//9 == 1:
                if not (whiteAbove((edge//9)*9+4)):
                    colors = RRCL.rotateSide(colors, edge//9)
                else:
                    colors = RRCL.rotateSide(colors, 0)
                
            else:
                colors = RRCL.rotateSide(colors, edgePieces[edge]//9)



       # if colors[edgePieces[edge]] == colors[edgePieces[edge]//6*6+4]:
       # if not (edgePieces[edge] >= 9 and edgePieces[edge] < 18) or (edge >= 9 and edge < 18):

             #   colors = RRCL.rotateSide(colors, colorOrder.index(colors[edgePieces[edge]]))

        




    else:

        step += 1

 


def whiteCrossB():
    global step
    global colors
    global algoritmIndex


       
    lastI = -1
    edges = []

    for x in range(4):
        while True:
            i = colors.index('white', lastI+1)
            lastI = i
            if i in edgePieces:
                edges.append(i)
                break


    notCorrectEdges = []
    notTopEdges = []


    
    for edge in edges:
        if not (colors[edgePieces[edge]] == colors[(edgePieces[edge]//9)*9+4]):
            notCorrectEdges.append(edge)
        if edge >= 9:
            notTopEdges.append(edge)


    if len(notCorrectEdges) > 2:
        colors = RRCL.rotateSide(colors, 0)

    if len(notCorrectEdges) == 2:
        
        
       # print(abs(whiteColorOrder.index(colors[edgePieces[notCorrectEdges[0]]]) - whiteColorOrder.index(colors[edgePieces[notCorrectEdges[1]]])))
        if abs(whiteColorOrder.index(colors[edgePieces[notCorrectEdges[0]]]) - whiteColorOrder.index(colors[edgePieces[notCorrectEdges[1]]])) == 2:

            step = 2
            algoritmIndex = 0
            

        else:
            step = 3
            algoritmIndex = 0

    if len(notCorrectEdges) == 0:
        algoritmIndex = 0
        step = 5

    
def doAlgorithm(a):
    global algoritmIndex
    global colors
    colors = RRCL.rotateSide(colors, a[algoritmIndex])



    algoritmIndex += 1




   # turn


algoritm = []
def whiteFinish():

    global step
    global colors
    global algoritmIndex, algoritm



       
    lastI = -1
    corners = []

    for x in range(4):
        while True:
            i = colors.index('white', lastI+1)
            lastI = i
            if i in cornerPieces:
                corners.append(i) 
                break


    notSolvedCorners = []
    notSolvedCorners

   # print(corners)
    for corner in corners:
      #  if corner >= 9:


        if not (colors[(corner//9)*9+4] == colors[corner] and colors[(cornerPieces[corner][0]//9)*9+4] == colors[cornerPieces[corner][0]] and colors[(cornerPieces[corner][1]//9)*9+4] == colors[cornerPieces[corner][1]]):
            notSolvedCorners.append(corner)


    possibleEdges = [['green','red'],['red','green'],['red','blue'],['blue','red'],['blue','orange'],['orange','blue'],['orange','green'],['green','orange']]
    notSolvedCorners.sort(key=lambda x: 
                          
                          possibleEdges.index([colors[cornerPieces[x][0]],colors[cornerPieces[x][1]]])
                          
                          
                          )



    if len(notSolvedCorners) > 0:
        corner = notSolvedCorners[0]
      
        topLayer = [0,1,2,3,4,5,6,7,8 ,45,46,47,18,19,20,36,37,38,33,34,35]
    # if notSolvedCorners[0] in topLayer: 
        # doAlgorithm([4,1,4,4,4,1,1,1])

    #  print([colors[(cornerPieces[corner][0]//9)*9+4], colors[(cornerPieces[corner][1]//9)*9+4]])
    #    print(colors[cornerPieces[corner][0]], colors[cornerPieces[corner][1]])


        c1 = cornerPieces[corner][0]
        c2 = cornerPieces[corner][1]
        cC1 = colors[c1]
        cC2 = colors[c2]


        edge = []
        if colors[(corner//9)*9+4] != 'yellow' and colors[(corner//9)*9+4] != 'white':
            edge.append(colors[(corner//9)*9+4])
        if colors[(c1//9)*9+4] != 'yellow' and colors[(c1//9)*9+4] != 'white':
            edge.append(colors[(cornerPieces[corner][0]//9)*9+4])
        if colors[(c2//9)*9+4] != 'yellow' and colors[(c2//9)*9+4] != 'white':
            edge.append(colors[(c2//9)*9+4])






        if ((cC1 in edge and cC2 in edge) or corner in topLayer) and algoritmIndex == 0 :
            
            # if min(whiteColorOrder.index(colors[cornerPieces[corner][0]]),whiteColorOrder.index(colors[cornerPieces[corner][1]])) == 0:
                # sideToRotate = 3
            #  else:
                    #sideToRotate = min(whiteColorOrder.index(colors[cornerPieces[corner][0]]),whiteColorOrder.index(colors[cornerPieces[corner][1]]))
            # print(colors[sideToRotate])

            if edge[0] in ['green', 'orange'] and edge[1] in ['green', 'orange']:
                sideToRotate = 2
                
            if edge[0] in ['red', 'blue'] and edge[1] in ['red', 'blue']:
                sideToRotate = 3
        
            if edge[0] in ['green', 'red'] and edge[1] in ['green', 'red']:
                sideToRotate = 4
            
            if edge[0] in ['blue', 'orange'] and edge[1] in ['blue', 'orange']:
                sideToRotate = 5


            algoritm = [sideToRotate,1,sideToRotate,sideToRotate,sideToRotate,1,1,1]

            



            # algoritm = [sideToRotate,1,sideToRotate,sideToRotate,sideToRotate,1,1,1]

            doAlgorithm(algoritm) 
            return

            # print(colors[sideToRotate*9+4])
        elif algoritmIndex != 0:
            if algoritmIndex < len(algoritm):
    
                doAlgorithm(algoritm) 
                return
            else:
                algoritmIndex = 0 
                return


        else:
            colors = RRCL.rotateSide(colors, 1)


    # if not (0 in notSolvedCorners) :
        # doAlgorithm([4,1,4,4,4,1,1,1])

        

       # print(notSolvedCorners)
    else:
        algoritmIndex = 0
        step += 1


def middleLayer():

    global step
    global colors
    global algoritmIndex, algoritm


    notCorrectEdges = 0
    if colors[21] != 'green' or colors[50] != 'orange':
        notCorrectEdges += 1
    if colors[23] != 'green' or colors[39] != 'red':
        notCorrectEdges += 1
    if colors[41] != 'red' or colors[32] != 'blue':
        notCorrectEdges += 1
    if colors[48] != 'orange' or colors[30] != 'blue':
        notCorrectEdges += 1




    if notCorrectEdges > 0:
        if algoritmIndex == 0:
         #   print(colors[25], colors[edgePieces[25]])
            if colors[25] == 'green' and colors[edgePieces[25]] == 'red':
                algoritm = [1, 4, 1,1,1, 4,4,4, 1,1,1, 2,2,2, 1, 2]
                doAlgorithm(algoritm)
               # print('green right')
            elif colors[25] == 'green' and colors[edgePieces[25]] == 'orange':
                algoritm = [1,1,1, 5,5,5 ,1,5,1, 2, 1,1,1, 2,2,2]
                doAlgorithm(algoritm)
              #  print('green left')
                #'''
            elif colors[28] == 'blue' and colors[edgePieces[28]] == 'orange':
                algoritm = [1, 4, 1,1,1, 4,4,4, 1,1,1, 3,3,3, 1, 3]
                doAlgorithm(algoritm)
            elif colors[28] == 'blue' and colors[edgePieces[28]] == 'red':
                algoritm = [1,1,1, 5,5,5 ,1,5,1, 3, 1,1,1, 3,3,3]
                doAlgorithm(algoritm)
                '''
            elif colors[43] == 'red' and colors[edgePieces[43]] == 'blue':
                print('red right')
            elif colors[43] == 'red' and colors[edgePieces[43]] == 'green':
                print('red left')

            elif colors[52] == 'orange' and colors[edgePieces[52]] == 'green':
                print('orange right')
            elif colors[52] == 'orange' and colors[edgePieces[52]] == 'blue':
                print('orange left')

                #'''

            else:

                colors = RRCL.rotateSide(colors, 1)

        else:
            if algoritmIndex < len(algoritm):
                doAlgorithm(algoritm)
            else:
                algoritmIndex = 0

    if notCorrectEdges == 0:

        algoritmIndex = 0
        step += 1






    






colors = ['white', 'yellow', 'blue', 'white', 'white', 'orange', 'blue', 'white', 'blue', 'yellow', 'yellow', 'white', 'blue', 'yellow', 'green', 'green', 'blue', 'white', 'yellow', 'green', 'yellow', 'white', 'green', 'green', 'red', 'green', 'green', 'yellow', 'yellow', 'blue', 'white', 'blue', 'blue', 'green', 'red', 'red', 'orange', 'yellow', 'white', 'orange', 'red', 'orange', 'orange', 'red', 'orange', 'red', 'blue', 'red', 'orange', 'orange', 'red', 'orange', 'red', 'green']





#colors = ['orange', 'red', 'red', 'red', 'white', 'white', 'orange', 'green', 'green', 'red', 'blue', 'blue', 'blue', 'yellow', 'blue', 'orange', 'orange', 'green', 'blue', 'orange', 'white', 'white', 'green', 'green', 'green', 'white', 'red', 'green', 'yellow', 'red', 'blue', 'blue', 'yellow', 'blue', 'green', 'blue', 'orange', 'red', 'yellow', 'white', 'red', 'green', 'white', 'yellow', 'white', 'yellow', 'yellow', 'white', 'orange', 'orange', 'orange', 'yellow', 'red', 'yellow']
#colors = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'blue', 'red', 'orange', 'yellow', 'green', 'yellow', 'yellow', 'red', 'green', 'green', 'green', 'blue', 'green', 'yellow', 'orange', 'red', 'blue', 'orange', 'orange', 'green', 'orange', 'blue', 'red', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'green', 'red', 'yellow', 'yellow', 'red', 'yellow', 'orange', 'orange', 'orange', 'green', 'orange', 'yellow', 'green', 'blue', 'blue']


#for x in range(20):
    #colors = RRCL.rotateSide(colors, random.randint(0,5))
# up down front back right left
angle = [0,0]




colorOrder = ['white', 'yellow', 'green', 'blue', 'red', 'orange']
whiteColorOrder = ['green', 'red', 'blue', 'orange']

#whiteCross(colors)


algoritmIndex = 0
font = pygame.font.Font(None,30)

step = 0

'''
for _ in range(1):

    colors = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
    
    step = 0
    algoritmIndex = 0

    turns = []

    for a in range(20):
        r = random.randint(0,5)
        colors = RRCL.rotateSide(colors, r)
        turns.append(r)

    ogSramble = colors.copy()


    i = 0
    while step != 6:

        if step == 0:
            whiteCrossA()
        elif step == 1:
            whiteCrossB()
        elif step == 2:
            if algoritmIndex < len([2,2,1,1,3,3,1,1,2,2]):
                doAlgorithm([2,2,1,1,3,3,1,1,2,2])
            else:
                whiteCrossB()
        
        elif step == 3:
            if algoritmIndex < len([4,4,1,2,2,1,1,1,4,4]):
                doAlgorithm([4,4,1,2,2,1,1,1,4,4])
            else: 
                whiteCrossB()
        elif step == 4:
            if algoritmIndex < len([4,4,1,2,2,1,1,1,4,4]):
                doAlgorithm([4,4,1,2,2,1,1,1,4,4])
            else: 
                whiteCrossB()
        

        elif step == 5:
            whiteFinish()



        i += 1
        if i > 10000:

            print(ogSramble)
            print(turns)
            exit()


#'''

        

#colors = RRCL.rotateSide(colors, 0)

time = 0
while True:
    mouse = False
    for event in pygame.event.get():     
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print(colors)
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True

        if event.type == pygame.KEYDOWN:

            if step == 0:
                whiteCrossA()
            elif step == 1:
                whiteCrossB()
            elif step == 2:
                if algoritmIndex < len([2,2,1,1,3,3,1,1,2,2]):
                    doAlgorithm([2,2,1,1,3,3,1,1,2,2])
                else:
                    whiteCrossB()
          
            elif step == 3:
                if algoritmIndex < len([4,4,1,2,2,1,1,1,4,4]):
                    doAlgorithm([4,4,1,2,2,1,1,1,4,4])
                else: 
                    whiteCrossB()
            elif step == 4:
                if algoritmIndex < len([4,4,1,2,2,1,1,1,4,4]):
                    doAlgorithm([4,4,1,2,2,1,1,1,4,4])
                else: 
                    whiteCrossB()

            

            elif step == 5:
                whiteFinish()

            elif step == 6:
                middleLayer()


            '''
            if event.key == pygame.K_0:
                colors = RRCL.rotateSide(colors, 0)
            if event.key == pygame.K_1:
                colors = RRCL.rotateSide(colors, 1)
            if event.key == pygame.K_2:
                colors = RRCL.rotateSide(colors, 2)
            if event.key == pygame.K_3:
                colors = RRCL.rotateSide(colors, 3)
            if event.key == pygame.K_4:
                colors = RRCL.rotateSide(colors, 4)
            if event.key == pygame.K_5:
                colors = RRCL.rotateSide(colors, 5)'''

                
    screen.fill((0,0,0))

  #  if not pygame.mouse.get_pressed()[0]:
      #  angle = [0,0]

    




    angle = RRCL.detectRotations(pygame.mouse.get_pressed(), pygame.mouse.get_rel() ,angle)



   # colors = RRCL.renderCube(list(range(0,54)), angle, screen, mouse, pygame.mouse.get_pos(), False)
    colors = RRCL.renderCube(colors, angle, screen, mouse, pygame.mouse.get_pos(), True)
   # if len(currentEdgeWorkingOn()) > 0:
      #  text = font.render(f'{colors[edgePieces[currentEdgeWorkingOn()[0]]]}', True, (255,255,255))
       # screen.blit(text, (0,0))

    text = font.render(f'{currentEdgeWorkingOn()}', True, (255,255,255))
    screen.blit(text, (0,20))


    text = font.render(f'{step}', True, (255,255,255))
    screen.blit(text, (0,40))

    text = font.render(f'{algoritmIndex}', True, (255,255,255))
    screen.blit(text, (0,60))

    pygame.display.update()
    time += 1