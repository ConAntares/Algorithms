#### My Colors and Colormaps: IRCA

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy
from matplotlib.colors import LinearSegmentedColormap

## Lines Colors

caBlack         = "#282828" # 040,040,040
caGray          = "#B4B4B4" # 180,180,180
caRed           = "#FF1E14" # 240,020,010
caPaleOrange    = "#E69650" # 230,150,080
caOrange        = "#FF7800" # 255,120,000
caGold          = "#FFC814" # 255,200,020
caSun           = "#FFC828" # 255,200,040
caYellow        = "#F0F000" # 240,240,000
caYellowGreen   = "#50D20F" # 080,210,015
caAshenGreen    = "#9BA546" # 155,165,070
caPaleGreen     = "#5FB946" # 095,185,070
caGreen         = "#32B432" # 050,180,050
caEmeraldGreen  = "#0FD264" # 015,215,100
caGreenEmerald  = "#1EDC78" # 030,210,120
caWarnEmerald   = "#19BE9B" # 025,190,155
caEmerald       = "#64CDCD" # 100,205,205
caEmeraldCyan   = "#96DCFA" # 150,220,250
caCyan          = "#00B4DC" # 000,180,220
caPaleCyanGreen = "#4BAF8C" # 075,175,140
caPaleCyanBlue  = "#4BAAA5" # 075,170,165
caPaleSky       = "#4BAABE" # 075,170,190
caSky           = "#00A0DC" # 000,160,220
caAzure         = "#28A0F5" # 040,160,245
caBlue          = "#1978F0" # 025,120,240
caPaleBlue      = "#64AADC" # 100,170,220
caDarkBlue      = "#3C78B4" # 060,120,180
caBlueViolet    = "#7864FA" # 120,120,250
caVioletBlue    = "#825AFF" # 130,090,255
caViolet        = "#A064DC" # 160,100,220
caPaleViolet    = "#B482EB" # 180,130,235
caPurple        = "#8C14C8" # 140,020,200
caPalePurple    = "#DC8CE6" # 220,140,230
caWarmPurple    = "#E691C8" # 230,145,200
caPink          = "#DC64C8" # 220,100,200
caPalePink      = "#F096A0" # 240,150,160
caBrown         = "#8C5A50" # 140,090,080
caAshen         = "#BEA04B" # 190,160,075

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

## Enjoy it !
## ✿✿ヽ(°▽°)ノ✿✿