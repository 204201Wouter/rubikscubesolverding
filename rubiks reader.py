import pygame
import cv2
import numpy as np
from sys import exit
import random
import math
import RRCL

pygame.init()
cap = cv2.VideoCapture(0)


width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Webcam Capture")

screenSize = screen.get_size()

screenCenter = [screenSize[0]/2, screenSize[1]/2]

# make color palet based on all colors availeble

colorPalet = [[255,0,0], # r
            [0,255,0], # gr
            [0,0,255], # b
            [255,255,255], # w
            [255,255,0], # ge
            [255,128,0] # o
            ]

#def makeColorPalet(colors):

   # if 


    #return colorPalet

def rgb2Name(color):
    #'''
    if color == colorPalet[0]:
        return 'red'
    if color == colorPalet[1]:
        return 'green'
    if color == colorPalet[2]:
        return 'blue'
    if color == colorPalet[3]:
        return 'white'
    if color == colorPalet[4]:
        return 'yellow'
    if color == colorPalet[5]:
        return 'orange'
    
    #'''

def distance(pointA, pointB):
    return ((pointA[0]-pointB[0])**2+(pointA[1]-pointB[1])**2+(pointA[2]-pointB[2])**2)**0.5

def closestColor(coord):

    '''
    minDistance = 200000
    minColor = None
    for color in colorPalet:
        d = distance(color, coord)
        if d < minDistance:
            minDistance = d
            minColor = color

    return rgb2Name(minColor)
    '''

# H  0,179  S  0,255   V 0, 255
    #'''
    color = coord
    #print(color)
    hsvcolor = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_RGB2HSV)[0][0]
    
   # print(hsvcolor)
    if hsvcolor[1] < 18/100*255: #and hsvcolor[2] > 40/100*255:
       # print('white')
        return 'white'
   # elif hsvcolor[2] < 20/100*255:
      #  print('black')
       # return 'black'
    elif hsvcolor[0] < 5 or hsvcolor[0] > 170:
       # print('red')
        return 'red'
    elif hsvcolor[0] < 20:
       # print('orange')
        return 'orange'
    elif hsvcolor[0] < 40:
       # print('yellow')
        return 'yellow'
    elif hsvcolor[0] < 85:
       # print('green')
        return 'green'
    elif hsvcolor[0] < 135:
       # print('blue')
        return 'blue'
    #'''
    return color


def calcColor(coords):
    colors = []
    for coord in coords:
        colors.append(getColor(coord))
    
    x,y,z = 0,0,0
    for color in colors:
        x+=color[0]
        y+=color[1]
        z+=color[2]

    x/=len(colors)
    y/=len(colors)
    z/=len(colors)

    return closestColor([x,y,z])

def getColor(coord):
    icoord = [int(coord[0]), int(coord[1])]
    
    rgbcolor = bFrame[icoord[0]][icoord[1]]
    return rgbcolor

def intersection(p1, p2, p3, p4):

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    D = dx1 * (-dy2) + dx2 * dy1


    t = ((x3 - x1) * (-dy2) + (y3 - y1) * dx2) / D

    ix = x1 + t * dx1
    iy = y1 + t * dy1

    return (ix, iy)


def pointonCube(pointa,pointb,factor):
    return pointa[0]+factor*(pointb[0]-pointa[0]), pointa[1]+factor*(pointb[1]-pointa[1])


def moveFaces(colors):


    colorOrder = ['white', 'yellow', 'green','blue' , 'red', 'orange']
        
    centers =[]
    sides = []

    for i in range(0,54,9):
        centers.append(i+4)
        sides.append([colors[i:i+9], colorOrder.index(colors[i+4])])


    #'''
    for i in range(len(sides)):
        cSide = sides[i][0].copy()
        
        sides[i][0][0] = cSide[6]
        sides[i][0][1] = cSide[7]
        sides[i][0][2] = cSide[8]
        sides[i][0][6] = cSide[0]
        sides[i][0][7] = cSide[1]
        sides[i][0][8] = cSide[2]
    #'''

    sides.sort(key=lambda x:x[1])


        

    fColor  = []
    for side in sides:

        for cell in side[0]:

            fColor.append(cell)
   # print(fColor)
   # return sides


   

   # print(centers)
  

 #   return colors


font = pygame.font.Font(None, 30)
running = True





fotos = [None,None]


vertexPos = []
mode = 'foto'
colors = []

fotoIndex = 0

while running:
    if mode == 'foto':
        ret, frame = cap.read()
        if not ret:
            break
        

        
        frame = np.rot90(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        fotos[fotoIndex] = frame

    
    frame = fotos[fotoIndex]
    bFrame = cv2.GaussianBlur(frame, (31, 31), 0)
    frame_surface = pygame.surfarray.make_surface(frame)

    screen.blit(frame_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
       

            if mode == 'select' and len(vertexPos) != 7:
                vertexPos.append(pygame.mouse.get_pos())
                if len(vertexPos) == 7:
                    pointssortedy = sorted(vertexPos, key=lambda x:x[1])
                    AenC = [pointssortedy[4], pointssortedy[5]]
                    edgespos = []
                    edgespos.append(min(AenC, key=lambda x:x[0]))
                    edgespos.append(pointssortedy[6])
                    edgespos.append(max(AenC, key=lambda x:x[0]))
                    edgespos.append(pointssortedy[3])
                    EenF = [pointssortedy[1], pointssortedy[2]]
                    edgespos.append(min(EenF, key=lambda x:x[0]))
                    edgespos.append(max(EenF, key=lambda x:x[0]) )  
                    edgespos.append(pointssortedy[0] )   

                                
                    linepoints = []


                    linepoints.append(pointonCube(edgespos[0], edgespos[1], 0.17))
                    linepoints.append(pointonCube(edgespos[0], edgespos[1], 0.5))
                    linepoints.append(pointonCube(edgespos[0], edgespos[1], 0.83))

                    linepoints.append(pointonCube(edgespos[1], edgespos[2], 0.17))
                    linepoints.append(pointonCube(edgespos[1], edgespos[2], 0.5))
                    linepoints.append(pointonCube(edgespos[1], edgespos[2], 0.83))

                    linepoints.append(pointonCube(edgespos[2], edgespos[3], 0.17))
                    linepoints.append(pointonCube(edgespos[2], edgespos[3], 0.5))
                    linepoints.append(pointonCube(edgespos[2], edgespos[3], 0.83))

                    linepoints.append(pointonCube(edgespos[3], edgespos[0], 0.17))
                    linepoints.append(pointonCube(edgespos[3], edgespos[0], 0.5))
                    linepoints.append(pointonCube(edgespos[3], edgespos[0], 0.83))


                    linepoints.append(pointonCube(edgespos[0], edgespos[4], 0.17))
                    linepoints.append(pointonCube(edgespos[0], edgespos[4], 0.5))
                    linepoints.append(pointonCube(edgespos[0], edgespos[4], 0.83))

                    linepoints.append(pointonCube(edgespos[4], edgespos[6], 0.17))
                    linepoints.append(pointonCube(edgespos[4], edgespos[6], 0.5))
                    linepoints.append(pointonCube(edgespos[4], edgespos[6], 0.83))

                    linepoints.append(pointonCube(edgespos[6], edgespos[3], 0.17))
                    linepoints.append(pointonCube(edgespos[6], edgespos[3], 0.5))
                    linepoints.append(pointonCube(edgespos[6], edgespos[3], 0.83))

                    linepoints.append(pointonCube(edgespos[6], edgespos[5], 0.17))
                    linepoints.append(pointonCube(edgespos[6], edgespos[5], 0.5))
                    linepoints.append(pointonCube(edgespos[6], edgespos[5], 0.83))

                    linepoints.append(pointonCube(edgespos[5], edgespos[2], 0.17))
                    linepoints.append(pointonCube(edgespos[5], edgespos[2], 0.5))
                    linepoints.append(pointonCube(edgespos[5], edgespos[2], 0.83))





                    colorPos = []
                    #'''
                    colorPos.append(intersection(linepoints[0],linepoints[8],linepoints[3],linepoints[11]))
                    colorPos.append(intersection(linepoints[1],linepoints[7],linepoints[3],linepoints[11]))
                    colorPos.append(intersection(linepoints[2],linepoints[6],linepoints[3],linepoints[11]))
                    colorPos.append(intersection(linepoints[0],linepoints[8],linepoints[4],linepoints[10]))
                    colorPos.append(intersection(linepoints[1],linepoints[7],linepoints[4],linepoints[10]))
                    colorPos.append(intersection(linepoints[2],linepoints[6],linepoints[4],linepoints[10]))
                    colorPos.append(intersection(linepoints[0],linepoints[8],linepoints[5],linepoints[9]))
                    colorPos.append(intersection(linepoints[1],linepoints[7],linepoints[5],linepoints[9]))
                    colorPos.append(intersection(linepoints[2],linepoints[6],linepoints[5],linepoints[9]))
                    #'''
                    colorPos.append(intersection(linepoints[11],linepoints[15],linepoints[12],linepoints[20]))
                    colorPos.append(intersection(linepoints[10],linepoints[16],linepoints[12],linepoints[20]))
                    colorPos.append(intersection(linepoints[9],linepoints[17],linepoints[12],linepoints[20]))
                    colorPos.append(intersection(linepoints[11],linepoints[15],linepoints[13],linepoints[19]))
                    colorPos.append(intersection(linepoints[10],linepoints[16],linepoints[13],linepoints[19]))
                    colorPos.append(intersection(linepoints[9],linepoints[17],linepoints[13],linepoints[19]))
                    colorPos.append(intersection(linepoints[11],linepoints[15],linepoints[14],linepoints[18]))
                    colorPos.append(intersection(linepoints[10],linepoints[16],linepoints[14],linepoints[18]))
                    colorPos.append(intersection(linepoints[9],linepoints[17],linepoints[14],linepoints[18]))

                    colorPos.append(intersection(linepoints[8],linepoints[21],linepoints[26],linepoints[20]))
                    colorPos.append(intersection(linepoints[7],linepoints[22],linepoints[26],linepoints[20]))
                    colorPos.append(intersection(linepoints[6],linepoints[23],linepoints[26],linepoints[20]))
                    colorPos.append(intersection(linepoints[8],linepoints[21],linepoints[25],linepoints[19]))
                    colorPos.append(intersection(linepoints[7],linepoints[22],linepoints[25],linepoints[19]))
                    colorPos.append(intersection(linepoints[6],linepoints[23],linepoints[25],linepoints[19]))
                    colorPos.append(intersection(linepoints[8],linepoints[21],linepoints[24],linepoints[18]))
                    colorPos.append(intersection(linepoints[7],linepoints[22],linepoints[24],linepoints[18]))
                    colorPos.append(intersection(linepoints[6],linepoints[23],linepoints[24],linepoints[18]))
                    
                    for pos in colorPos:
                        colors.append(calcColor([pos]))

            if len(vertexPos) == 7:
                mouse = pygame.mouse.get_pos()
                for i, pos in enumerate(colorPos):
                    allColors = ['white', 'yellow', 'green', 'blue', 'red', 'orange']
            
                    if distance([pos[0], pos[1], 0], [mouse[0], mouse[1], 0]) < 10:
                        index = (allColors.index(colors[fotoIndex*27+i])+1)%len(allColors)
                

                        colors[fotoIndex*27+i] = allColors[index]
                
                                



        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(colors) == 54:
              #  moveFaces(colors)
               # exit()
               running = False
            if mode == 'foto':
                fotoIndex += 1
                if fotoIndex == 2:
                    mode = 'select'
                    fotoIndex = 0
            if len(vertexPos) == 7:
                vertexPos = []
                fotoIndex += 1
         





    for pos in vertexPos:
        pygame.draw.circle(screen, (255,255,255), pos, 5)


    if len(vertexPos) == 7 :


        i = 0
        for pos in colorPos:
            pygame.draw.circle(screen, getColor(pos), pos, 10)

            pygame.draw.circle(screen, colors[fotoIndex*27+i], pos, 2)
            i+=1
           



  



    pygame.display.update()





size = 20
def drawFace(face, pos):
    coords = [[0,0], [size,0], [size*2,0], [size*3,0], [size*4,0], [0,size], [size,size], [size*2,size], [size*3,size], [size*4,size], [0,size*2], [size,size*2], [size*2,size*2], [size*3,size*2], [size*4,size*2], [0,size*3], [size,size*3], [size*2,size*3], [size*3,size*3], [size*4,size*3], [0,size*4], [size,size*4], [size*2,size*4], [size*3,size*4], [size*4,size*4]]
    for color, coord in zip(face, coords):
        if color == '0':
            pygame.draw.rect(screen, (0,0,0), (coord[0]+pos[0], coord[1]+pos[1], size,size))
        else:
            pygame.draw.rect(screen, color, (coord[0]+pos[0], coord[1]+pos[1], size,size))





def mirrorFace(face):
    npSide = np.array(face).reshape((3, 3))

    fSide = np.fliplr(npSide).flatten()


    return fSide.tolist()

def rotateFace(face):
    if len(face) == 25:
        npSide = np.array(face).reshape((5, 5))
    if len(face) == 9:
        npSide = np.array(face).reshape((3, 3))

    rSide = np.rot90(npSide).flatten()


    return rSide.tolist()

centers = []
for i in range(6):
    face = colors[i*9:i*9+9]
    mFace = face#mirrorFace(face)
    centers.append(colors[i*9+4])

    for i2 in range(9):
        colors[i*9+i2] = mFace[i2]

colorOrder = ['white', 'yellow', 'green','blue' , 'red', 'orange']
def revColor(color):
    
    revColorOrder = ['yellow', 'white', 'blue','green' , 'orange', 'red']
    
    return revColorOrder[colorOrder.index(color)]


directions = [
[     centers.index(revColor(centers[2]))*9, 9,   18,   centers.index(revColor(centers[1]))*9],
[    0,    centers.index(revColor(centers[2]))*9, centers.index(revColor(centers[0]))*9,  18],
[    0,    9,   centers.index(revColor(centers[0]))*9,  centers.index(revColor(centers[1]))*9],
[    centers.index(revColor(centers[5]))*9, 36,   45,   centers.index(revColor(centers[4]))*9],
[    27,   centers.index(revColor(centers[5]))*9, centers.index(revColor(centers[3]))*9, 45],
[    27,   36,   centers.index(revColor(centers[3]))*9, centers.index(revColor(centers[4]))*9]
]



faces = []
for i in range(6):

    face = colors[i*9:i*9+9]
    d = directions[i].copy()



    faces.append([
        0,0,          colors[d[0]+4],        0,0,
        0,   face[0],face[1],face[2],0,
        colors[d[1]+4],face[3],face[4],face[5],colors[d[3]+4],
        0,   face[6],face[7],face[8],0,
        0,0,          colors[d[2]+4],        0,0
    ])




facesCopy = []
for face in faces:
    facesCopy.append(face.copy())


for i, color in enumerate(colorOrder):

    fI = centers.index(color)
    cFace = facesCopy[fI]
    faces[i] =  cFace



while faces[0][22] != faces[2][12]:
    faces[0] = rotateFace(faces[0])
while faces[1][2] != faces[2][12]:
    faces[1] = rotateFace(faces[1])
while faces[2][2] != faces[0][12]:
    faces[2] = rotateFace(faces[2])
while faces[3][2] != faces[1][12]:
    faces[3] = rotateFace(faces[3])
while faces[4][10] != faces[2][12]:
    faces[4] = rotateFace(faces[4])
while faces[5][14] != faces[2][12]:
    faces[5] = rotateFace(faces[5])




def convertBack(faces):

    newFaces = []
    for face in faces:
        newFaces.append(face[6])
        newFaces.append(face[7])
        newFaces.append(face[8])
        newFaces.append(face[11])
        newFaces.append(face[12])
        newFaces.append(face[13])
        newFaces.append(face[16])
        newFaces.append(face[17])
        newFaces.append(face[18])
     
            
        

   # print(newFaces)


    return newFaces


colors = convertBack(faces)
print(colors)

angle = [0,0]





while True:
    mouse = False
    for event in pygame.event.get():     
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print(colors)
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True


                
    screen.fill((0,0,0))

    angle = RRCL.detectRotations(pygame.mouse.get_pressed(), pygame.mouse.get_rel() ,angle)


  #  colors = RRCL.rotateSide()


    colors = RRCL.renderCube(colors, angle, screen, mouse, pygame.mouse.get_pos(), False)



    pygame.display.update()