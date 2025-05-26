
import math
import pygame
import random
import numpy as np






def project(coord, screen):
    return [(coord[0])/(coord[2]-10)*1000+screen.get_size()[0]/2, (coord[1])/(coord[2]-10)*1000+screen.get_size()[1]/2]




def rotate(coord, angle):
    rCoord = rotateAxis(coord, angle[0], "y")
    rCoord = rotateAxis(rCoord, angle[1], "x")
    return rCoord


def rotateAxis(point, angle, axis):
   
    x, y, z = point
    cosA = math.cos(angle)
    sinA = math.sin(angle)
    
    if axis == 'x':
        rY = y * cosA - z * sinA
        rZ = y * sinA + z * cosA
        return [x, rY, rZ]
    elif axis == 'y':
        rX = x * cosA + z * sinA
        rZ = -x * sinA + z * cosA
        return [rX, y, rZ]
    elif axis == 'z':
        rX = x * cosA - y * sinA
        rY = x * sinA + y * cosA
        return [rX, rY, z]
    



def renderCube(colors, angle, screen, mouse, mousePos, changingColors):



    coords = [
        # Up face (y = 1)  
        [0.35, 1, -0.98], [0.98, 1, -0.98], [0.98, 1, -0.35], [0.35, 1, -0.35],      # (square 38)
        [-0.31, 1, -0.98], [0.31, 1, -0.98], [0.31, 1, -0.35], [-0.31, 1, -0.35],    # (square 37)
        [-0.98, 1, -0.98], [-0.35, 1, -0.98], [-0.35, 1, -0.35], [-0.98, 1, -0.35],  # (square 36)
        [0.35, 1, -0.31], [0.98, 1, -0.31], [0.98, 1, 0.31], [0.35, 1, 0.31],        # (square 41)
        [-0.31, 1, -0.31], [0.31, 1, -0.31], [0.31, 1, 0.31], [-0.31, 1, 0.31],      # (square 40)
        [-0.98, 1, -0.31], [-0.35, 1, -0.31], [-0.35, 1, 0.31], [-0.98, 1, 0.31],    # (square 39)
        [0.35, 1, 0.35], [0.98, 1, 0.35], [0.98, 1, 0.98], [0.35, 1, 0.98],          # (square 44)
        [-0.31, 1, 0.35], [0.31, 1, 0.35], [0.31, 1, 0.98], [-0.31, 1, 0.98],        # (square 43)
        [-0.98, 1, 0.35], [-0.35, 1, 0.35], [-0.35, 1, 0.98], [-0.98, 1, 0.98],      # (square 42)

        # Down face (y = -1)  
        [0.35, -1, 0.98], [0.98, -1, 0.98], [0.98, -1, 0.35], [0.35, -1, 0.35],      # (square 47)
        [-0.31, -1, 0.98], [0.31, -1, 0.98], [0.31, -1, 0.35], [-0.31, -1, 0.35],    # (square 46)
        [-0.98, -1, 0.98], [-0.35, -1, 0.98], [-0.35, -1, 0.35], [-0.98, -1, 0.35],  # (square 45)   
        [0.35, -1, 0.31], [0.98, -1, 0.31], [0.98, -1, -0.31], [0.35, -1, -0.31],    # (square 50)
        [-0.31, -1, 0.31], [0.31, -1, 0.31], [0.31, -1, -0.31], [-0.31, -1, -0.31],  # (square 49)
        [-0.98, -1, 0.31], [-0.35, -1, 0.31], [-0.35, -1, -0.31], [-0.98, -1, -0.31],# (square 48)
        [0.35, -1, -0.35], [0.98, -1, -0.35], [0.98, -1, -0.98], [0.35, -1, -0.98],   # (square 53)
        [-0.31, -1, -0.35], [0.31, -1, -0.35], [0.31, -1, -0.98], [-0.31, -1, -0.98],# (square 52)
        [-0.98, -1, -0.35], [-0.35, -1, -0.35], [-0.35, -1, -0.98], [-0.98, -1, -0.98],# (square 51)

        # Front face (z = 1)
        [0.35, 0.98, 1], [0.98, 0.98, 1], [0.98, 0.35, 1], [0.35, 0.35, 1],          # Top-right (square 2)
        [-0.31, 0.98, 1], [0.31, 0.98, 1], [0.31, 0.35, 1], [-0.31, 0.35, 1],        # Top-middle (square 1)
        [-0.98, 0.98, 1], [-0.35, 0.98, 1], [-0.35, 0.35, 1], [-0.98, 0.35, 1],     # Top-left (square 0)
        [0.35, 0.31, 1], [0.98, 0.31, 1], [0.98, -0.31, 1], [0.35, -0.31, 1],        # Middle-right (square 5)
        [-0.31, 0.31, 1], [0.31, 0.31, 1], [0.31, -0.31, 1], [-0.31, -0.31, 1],      # Center (square 4)
        [-0.98, 0.31, 1], [-0.35, 0.31, 1], [-0.35, -0.31, 1], [-0.98, -0.31, 1],    # Middle-left (square 3)
        [0.35, -0.35, 1], [0.98, -0.35, 1], [0.98, -0.98, 1], [0.35, -0.98, 1],      # Bottom-right (square 8)
        [-0.31, -0.35, 1], [0.31, -0.35, 1], [0.31, -0.98, 1], [-0.31, -0.98, 1],    # Bottom-middle (square 7)
        [-0.98, -0.35, 1], [-0.35, -0.35, 1], [-0.35, -0.98, 1], [-0.98, -0.98, 1],  # Bottom-left (square 6)

        # Back face (z = -1)  
        [0.98, -0.35, -1], [0.35, -0.35, -1], [0.35, -0.98, -1], [0.98, -0.98, -1],  # (square 15)
        [0.31, -0.35, -1], [-0.31, -0.35, -1], [-0.31, -0.98, -1], [0.31, -0.98, -1],# (square 16)
        [-0.35, -0.35, -1], [-0.98, -0.35, -1], [-0.98, -0.98, -1], [-0.35, -0.98, -1],# (square 17)
        [0.98, 0.31, -1], [0.35, 0.31, -1], [0.35, -0.31, -1], [0.98, -0.31, -1],    # (square 12)
        [0.31, 0.31, -1], [-0.31, 0.31, -1], [-0.31, -0.31, -1], [0.31, -0.31, -1],  # (square 13)
        [-0.35, 0.31, -1], [-0.98, 0.31, -1], [-0.98, -0.31, -1], [-0.35, -0.31, -1],# (square 14)
        [0.98, 0.98, -1], [0.35, 0.98, -1], [0.35, 0.35, -1], [0.98, 0.35, -1],      # (square 9)
        [0.31, 0.98, -1], [-0.31, 0.98, -1], [-0.31, 0.35, -1], [0.31, 0.35, -1],    # (square 10)
        [-0.35, 0.98, -1], [-0.98, 0.98, -1], [-0.98, 0.35, -1], [-0.35, 0.35, -1],  # (square 11)


        # Left face (x = -1)  
        [-1, 0.98, 0.98], [-1, 0.98, 0.35], [-1, 0.35, 0.35], [-1, 0.35, 0.98],      # (square 18)
        [-1, 0.98, 0.31], [-1, 0.98, -0.31], [-1, 0.35, -0.31], [-1, 0.35, 0.31],    # (square 19)
        [-1, 0.98, -0.35], [-1, 0.98, -0.98], [-1, 0.35, -0.98], [-1, 0.35, -0.35],  # (square 20)
        [-1, 0.31, 0.98], [-1, 0.31, 0.35], [-1, -0.31, 0.35], [-1, -0.31, 0.98],    # (square 21)
        [-1, 0.31, 0.31], [-1, 0.31, -0.31], [-1, -0.31, -0.31], [-1, -0.31, 0.31],  # (square 22)
        [-1, 0.31, -0.35], [-1, 0.31, -0.98], [-1, -0.31, -0.98], [-1, -0.31, -0.35],# (square 23)
        [-1, -0.35, 0.98], [-1, -0.35, 0.35], [-1, -0.98, 0.35], [-1, -0.98, 0.98],  # (square 24)
        [-1, -0.35, 0.31], [-1, -0.35, -0.31], [-1, -0.98, -0.31], [-1, -0.98, 0.31],# (square 25)
        [-1, -0.35, -0.35], [-1, -0.35, -0.98], [-1, -0.98, -0.98], [-1, -0.98, -0.35],# (square 26)

        # Right face (x = 1)  
        [1, 0.98, -0.98], [1, 0.98, -0.35], [1, 0.35, -0.35], [1, 0.35, -0.98],      # (square 27)
        [1, 0.98, -0.31], [1, 0.98, 0.31], [1, 0.35, 0.31], [1, 0.35, -0.31],        # (square 28)
        [1, 0.98, 0.35], [1, 0.98, 0.98], [1, 0.35, 0.98], [1, 0.35, 0.35],          # (square 29)
        [1, 0.31, -0.98], [1, 0.31, -0.35], [1, -0.31, -0.35], [1, -0.31, -0.98],    # (square 30)
        [1, 0.31, -0.31], [1, 0.31, 0.31], [1, -0.31, 0.31], [1, -0.31, -0.31],      # (square 31)
        [1, 0.31, 0.35], [1, 0.31, 0.98], [1, -0.31, 0.98], [1, -0.31, 0.35],        # (square 32)
        [1, -0.35, -0.98], [1, -0.35, -0.35], [1, -0.98, -0.35], [1, -0.98, -0.98],  # (square 33)
        [1, -0.35, -0.31], [1, -0.35, 0.31], [1, -0.98, 0.31], [1, -0.98, -0.31],    # (square 34)
        [1, -0.35, 0.35], [1, -0.35, 0.98], [1, -0.98, 0.98], [1, -0.98, 0.35],      # (square 35)



    ]


    reference = [
        # Front face (z = 1)
        [
            [0, 1, 2, 3],     # Top-left
            [4, 5, 6, 7],     # Top-middle
            [8, 9, 10, 11],    # Top-right
            [12, 13, 14, 15],  # Middle-left
            [16, 17, 18, 19],  # Center
            [20, 21, 22, 23],  # Middle-right
            [24, 25, 26, 27],  # Bottom-left
            [28, 29, 30, 31],  # Bottom-middle
            [32, 33, 34, 35]  # Normal
        ],

        # Back face (z = -1)
        [
            [36, 37, 38, 39],  # Top-left
            [40, 41, 42, 43],  # Top-middle
            [44, 45, 46, 47],  # Top-right
            [48, 49, 50, 51],  # Middle-left
            [52, 53, 54, 55],  # Center
            [56, 57, 58, 59],  # Middle-right
            [60, 61, 62, 63],  # Bottom-left
            [64, 65, 66, 67],  # Bottom-middle
            [68, 69, 70, 71]  
        ],

        # Left face (x = -1)
        [
            [72, 73, 74, 75],  # Top-left
            [76, 77, 78, 79],  # Top-middle
            [80, 81, 82, 83],  # Top-right
            [84, 85, 86, 87],  # Middle-left
            [88, 89, 90, 91],  # Center
            [92, 93, 94, 95],  # Middle-right
            [96, 97, 98, 99],  # Bottom-left
            [100, 101, 102, 103],  # Bottom-middle
            [104, 105, 106, 107]
        ],

        # Right face (x = 1)
        [
            [108, 109, 110, 111],  # Top-left
            [112, 113, 114, 115],  # Top-middle
            [116, 117, 118, 119],  # Top-right
            [120, 121, 122, 123],  # Middle-left
            [124, 125, 126, 127],  # Center
            [128, 129, 130, 131],  # Middle-right
            [132, 133, 134, 135],  # Bottom-left
            [136, 137, 138, 139],  # Bottom-middle
            [140, 141, 142, 143]
        ],

        # Up face (y = 1)
        [
            [144, 145, 146, 147],  # Top-left
            [148, 149, 150, 151],  # Top-middle
            [152, 153, 154, 155],  # Top-right
            [156, 157, 158, 159],  # Middle-left
            [160, 161, 162, 163],  # Center
            [164, 165, 166, 167],  # Middle-right
            [168, 169, 170, 171],  # Bottom-left
            [172, 173, 174, 175],  # Bottom-middle
            [176, 177, 178, 179]
        ],

        # Down face (y = -1)
        [
            [180, 181, 182, 183],  # Top-left
            [184, 185, 186, 187],  # Top-middle
            [188, 189, 190, 191],  # Top-right
            [192, 193, 194, 195],  # Middle-left
            [196, 197, 198, 199],  # Center
            [200, 201, 202, 203],  # Middle-right
            [204, 205, 206, 207],  # Bottom-left
            [208, 209, 210, 211],  # Bottom-middle
            [212, 213, 214, 215]
        ]
    ]


    i = 0
    polygons = []


    
    for side in reference:


        for cell in side:
            
            
            pCoords = []
            rCoords = []

            for coord in cell:
                rCoord = rotate(coords[coord], angle)
                
            


                if rCoord[2] > -10:
                
                    
                    pCoord = project(rCoord, screen)
                    pCoords.append(pCoord)
                    rCoords.append(rCoord[2])

            if len(pCoords) == 4:

                
    

                polygons.append([i, pCoords, sum(rCoords)])
                


            i += 1



    polygons.sort(reverse=False, key=lambda x:x[2])


    allColors = ['white', 'yellow', 'green', 'blue', 'red', 'orange']

    selectedPolygons = None
    for polygon in polygons:
       # print(polygon[0])
        if type(colors[0]) == str:

            pygame.draw.polygon(screen, colors[polygon[0]], polygon[1])
        else:
            pygame.draw.polygon(screen, (colors[polygon[0]]%9*30, colors[polygon[0]]%9*30, colors[polygon[0]]%9*30), polygon[1])

        if mouse and changingColors:
            if isPointInPolygon(polygon[1], mousePos):
                selectedPolygons = polygon[0]
              

                #next
               # print(colors[polygon[0]])


    if selectedPolygons != None:
        
        index = (allColors.index(colors[selectedPolygons])+1)%len(allColors)

        colors[selectedPolygons] = allColors[index]
 
       # colors[polygon[0]] = 'black'


    return colors

def isPointInPolygon(polygon, point):
    def on_left(p1, p2, p):
        return (p2[0] - p1[0]) * (p[1] - p1[1]) > (p2[1] - p1[1]) * (p[0] - p1[0])

    p1, p2, p3, p4 = polygon
    
    inside = (on_left(p1, p2, point) == on_left(p2, p3, point) == on_left(p3, p4, point) == on_left(p4, p1, point))
    
    return inside



def detectRotations(mouse, mouseRel, angle):

 
    if mouse[0] :
        if angle[1]  > math.radians(90) and angle[1]  < math.radians(270):
            angle[0] += mouseRel[0]/50
        else:
            angle[0] += -mouseRel[0]/50
        angle[1] += mouseRel[1]/50

    
    angle[1] %= math.radians(360)

    return(angle)


        
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

def rotateSide(colors, rotation):

    
    '''
    side = [
            None,edgePieces[rotation+0], edgePieces[rotation+1], edgePieces[rotation+2], None,
            edgePieces[rotation+0],  rotation+0, rotation+1, rotation+2, edgePieces[rotation+2],
            edgePieces[rotation+3],  rotation+3, rotation+4, rotation+5, edgePieces[rotation+5],
            edgePieces[rotation+6],  rotation+6, rotation+7, rotation+8, edgePieces[rotation+8],
            None,edgePieces[rotation+6], edgePieces[rotation+7], edgePieces[rotation+8], None  
                ]
    ''' 

        
    if rotation % 6 == 0: # white

        side = [
            None,33, 34, 35, None,
            45,  0, 1, 2, 38,
            46,  3, 4, 5, 37,
            47,  6, 7, 8, 36,
            None,18, 19, 20, None  
                ]
        
    if rotation % 6 == 1: # yellow
        side = [
            None,2*9+6, 2*9+7, 2*9+8, None,
            5*9+8,  9, 10, 11, 4*9+6,
            5*9+7,  12, 13, 14, 4*9+7,
            5*9+6,  15, 16, 17, 4*9+8,
            None,3*9+0, 3*9+1, 3*9+2, None  
                ]
        
    # working until this
        
    if rotation % 6 == 2: # green
        side = [
            None,6, 7, 8, None,
            47,  18, 19, 20, 36,
            50,  21, 22, 23, 39,
            53,  24, 25, 26, 42,
            None,9, 10, 11, None  
                ]
        
    if rotation % 6 == 3: # blue
        side = [
            None,15, 16, 17, None,
            51,  27, 28, 29, 44,
            48,  30, 31, 32, 41,
            45,  33, 34, 35, 38,
            None,0, 1, 2, None  
                ]
        
    if rotation % 6 == 4: # red
        side = [
            None,8, 5, 2, None,
            20,  36, 37, 38, 35,
            23,  39, 40, 41, 32,
            26,  42, 43, 44, 29,
            None,11, 14, 17, None  
                ]

    if rotation % 6 == 5: # orange
        side = [
            None,0, 3, 6, None,
            33,  45, 46, 47, 18,
            30,  48, 49, 50, 21,
            27,  51, 52, 53, 24,
            None,15, 12, 9, None  
                ]
        
        
    
    cSide = side.copy()
    cSide = np.array(cSide).reshape((5, 5))
    for _ in range((rotation // 6) + 1):
        cSide = np.rot90(cSide)
    
    cSide = cSide.flatten().tolist()
    cColors = colors.copy()
    for cell, cCell in zip(side,cSide):
        if cell != None:
            colors[cell] = cColors[cCell]




    return colors



def rotateSide2x2(colors, rotation):

    

        
    if rotation % 6 == 0: # white

        side = [
            None ,14, 15, None,
            20,  0, 1, 17,
            21,  2, 3, 16,
            None,8, 9, None  
                ]
        
        
    if rotation % 6 == 1: # green
        side = [
            None ,10, 11, None,
            23,  4, 5, 18,
            22,  6, 7, 19,
            None,12, 13, None  
                ]
        
    if rotation % 6 == 2: # blue
        side = [
            None ,2, 3, None,
            21,  8, 9, 16,
            23,  10, 11, 18,
            None,4, 5, None  
                ]
        
    if rotation % 6 == 3: # red
        side = [
            None ,6, 7, None,
            22,  12, 13, 19,
            20,  14, 15, 17,
            None,0, 1, None  
                ]

    if rotation % 6 == 4: # orange
        side = [
            None ,3, 1, None,
            9,  16, 17, 15,
            11,  18, 19, 13,
            None,5, 7, None  
                ]

    if rotation % 6 == 5: # orange
        side = [
            None ,0, 2, None,
            14,  20, 21, 8,
            12,  22, 23, 10,
            None,6, 4, None  
                ]    
        
    
    cSide = side.copy()
    cSide = np.array(cSide).reshape((4, 4))
    for _ in range((rotation // 6) + 1):
        cSide = np.rot90(cSide)

        
    
    cSide = cSide.flatten().tolist()
    cColors = colors.copy()

    for cell, cCell in zip(side,cSide):
        if cell != None:
  
            colors[cell] = cColors[cCell]




    return colors

