#### My Colormap: IRCA

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy
from matplotlib.colors import LinearSegmentedColormap

## Lines Colors

myBlack     = "#282828" # 040,040,040
myGary      = "#B4B4B4" # 180,180,180
myRed       = "#FF1E14" # 240,020,010
myOrange    = "#FF7800" # 255,120,000
myGold      = "#FFC814" # 255,200,020
myYellow    = "#F0F000" # 240,240,000
myGreen     = "#32B432" # 050,180,050
myEmerald   = "#64CDCD" # 100,205,205
myCyan      = "#00B4DC" # 000,180,220
mySky       = "#00A0DC" # 000,160,220
myBlue      = "#1978BE" # 025,120,190
myDarkBlue  = "#3C78B4" # 060,120,180
myViolet    = "#A064DC" # 160,100,220
myPurple    = "#8C14C8" # 140,020,200
myPink      = "#DC64C8" # 220,100,200
myBrown     = "#8C5A50" # 140,090,080

## IR CA Color Map

irca = {'red':  ((0.0,  15/255,  15/255),
                 (0.1,  25/255,  25/255),
                 (0.2,  10/255,  10/255),
                 (0.3,  30/255,  30/255),
                 (0.4, 100/255, 100/255),
                 (0.5, 180/255, 180/255),
                 (0.6, 240/255, 240/255),
                 (0.7, 255/255, 255/255),
                 (0.8, 255/255, 255/255),
                 (0.9, 250/255, 250/255),
                 (1.0, 230/255, 230/255)),
        'green':((0.0,  60/255,  60/255),
                 (0.1,  75/255,  75/255),
                 (0.2, 130/255, 130/255),
                 (0.3, 180/255, 180/255),
                 (0.4, 240/255, 240/255),
                 (0.5, 245/255, 245/255),
                 (0.6, 240/255, 240/255),
                 (0.7, 180/255, 180/255),
                 (0.8,  80/255,  80/255),
                 (0.9,  60/255,  60/255),
                 (1.0,  25/255,  25/255)),
        'blue': ((0.0,  90/255,  90/255),
                 (0.1, 120/255, 120/255),
                 (0.2, 150/255, 150/255),
                 (0.3, 110/255, 110/255),
                 (0.4,  80/255,  80/255),
                 (0.5, 160/255, 160/255),
                 (0.6,   0/255,   0/255),
                 (0.7,   0/255,   0/255),
                 (0.8,   0/255,   0/255),
                 (0.9,   0/255,   0/255),
                 (1.0,  10/255,  10/255))}

## IR CA Line Color Map

ircal = {'red': ((0.0,  15/255,  15/255),
                 (0.1,  25/255,  25/255),
                 (0.2,  10/255,  10/255),
                 (0.3,  30/255,  30/255),
                 (0.4, 100/255, 100/255),
                 (0.5, 180/255, 180/255),
                 (0.6, 240/255, 240/255),
                 (0.7, 255/255, 255/255),
                 (0.8, 255/255, 255/255),
                 (0.9, 250/255, 250/255),
                 (1.0, 230/255, 230/255)),
        'green':((0.0,  60/255,  60/255),
                 (0.1,  75/255,  75/255),
                 (0.2, 130/255, 130/255),
                 (0.3, 180/255, 180/255),
                 (0.4, 240/255, 240/255),
                 (0.5, 180/255, 180/255),
                 (0.6, 240/255, 240/255),
                 (0.7, 180/255, 180/255),
                 (0.8,  80/255,  80/255),
                 (0.9,  60/255,  60/255),
                 (1.0,  25/255,  25/255)),
        'blue': ((0.0,  90/255,  90/255),
                 (0.1, 120/255, 120/255),
                 (0.2, 150/255, 150/255),
                 (0.3, 110/255, 110/255),
                 (0.4,  80/255,  80/255),
                 (0.5, 180/255, 180/255),
                 (0.6,   0/255,   0/255),
                 (0.7,   0/255,   0/255),
                 (0.8,   0/255,   0/255),
                 (0.9,   0/255,   0/255),
                 (1.0,  10/255,  10/255))}

## IR CA Diverging Color Map

ircad = {'red': ((0.0,  15/255,  15/255),
                 (0.1,  25/255,  25/255),
                 (0.2,  12/255,  12/255),
                 (0.3,  40/255,  40/255),
                 (0.4, 160/255, 160/255),
                 (0.5, 255/255, 255/255),
                 (0.6, 255/255, 255/255),
                 (0.7, 255/255, 255/255),
                 (0.8, 255/255, 255/255),
                 (0.9, 250/255, 250/255),
                 (1.0, 230/255, 230/255)),
        'green':((0.0,  60/255,  60/255),
                 (0.1,  75/255,  75/255),
                 (0.2, 140/255, 140/255),
                 (0.3, 200/255, 200/255),
                 (0.4, 240/255, 240/255),
                 (0.5, 255/255, 255/255),
                 (0.6, 240/255, 240/255),
                 (0.7, 180/255, 180/255),
                 (0.8,  90/255,  90/255),
                 (0.9,  60/255,  60/255),
                 (1.0,  25/255,  25/255)),
        'blue': ((0.0,  90/255,  90/255),
                 (0.1, 120/255, 120/255),
                 (0.2, 170/255, 170/255),
                 (0.3, 160/255, 160/255),
                 (0.4, 180/255, 180/255),
                 (0.5, 255/255, 255/255),
                 (0.6,  80/255,  80/255),
                 (0.7,  40/255,  40/255),
                 (0.8,   0/255,   0/255),
                 (0.9,   0/255,   0/255),
                 (1.0,  10/255,  10/255))}

## IR CA Cold Color Map 1

ircac1 = {'red':((0.0,  15/255,  15/255),
                 (0.2,  25/255,  25/255),
                 (0.4,  12/255,  12/255),
                 (0.6,  40/255,  40/255),
                 (0.8, 160/255, 160/255),
                 (1.0, 255/255, 255/255)),
        'green':((0.0,  60/255,  60/255),
                 (0.2,  75/255,  75/255),
                 (0.4, 140/255, 140/255),
                 (0.6, 200/255, 200/255),
                 (0.8, 240/255, 240/255),
                 (1.0, 255/255, 255/255)),
        'blue': ((0.0,  90/255,  90/255),
                 (0.2, 120/255, 120/255),
                 (0.4, 170/255, 170/255),
                 (0.6, 160/255, 160/255),
                 (0.8, 180/255, 180/255),
                 (1.0, 255/255, 255/255))}

## IR CA Cold Color Map 2

ircac2 = {'red':((0.0, 255/255, 255/255),
                 (0.2, 160/255, 160/255),
                 (0.4,  40/255,  40/255),
                 (0.6,  12/255,  12/255),
                 (0.8,  25/255,  25/255),
                 (1.0,  15/255,  15/255)),
        'green':((0.0, 255/255, 255/255),
                 (0.2, 240/255, 240/255),
                 (0.4, 200/255, 200/255),
                 (0.6, 140/255, 140/255),
                 (0.8,  75/255,  75/255),
                 (1.0,  60/255,  60/255)),
        'blue': ((0.0, 255/255, 255/255),
                 (0.2, 180/255, 180/255),
                 (0.4, 160/255, 160/255),
                 (0.6, 170/255, 170/255),
                 (0.8, 120/255, 120/255),
                 (1.0,  90/255,  90/255),)}

irca   = LinearSegmentedColormap("IR CA",irca)
ircal  = LinearSegmentedColormap("IR CA Line",ircal)
ircad  = LinearSegmentedColormap("IR CA Diverging",ircad)
#ircah1 = LinearSegmentedColormap("IR CA Hot1",ircah1)
#ircah2 = LinearSegmentedColormap("IR CA Hot2",ircah2)
ircac1 = LinearSegmentedColormap("IR CA Cold",ircac1)
ircac2 = LinearSegmentedColormap("IR CA Cold",ircac2)