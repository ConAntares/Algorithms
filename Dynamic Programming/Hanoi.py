#### Hanoi

import time

to = time.time()

def hanoi(plate_number,x,y,z):
    if plate_number == 1:
        print(x, "=>", z)               #   Output the movement from X to Z with Y
    else:
        hanoi(plate_number-1,x,z,y)     #   move the top plates from X to Y with Z
        hanoi(1,x,y,z)                  #   move the last plate from X to Z with Y
        hanoi(plate_number-1,y,x,z)     #   move the top plates from Y to Z with X

n = int(input("Please input the number of oder. \n"))
hanoi(n,"1st Pin","2nd Pin","3rd Pin")

td = time.time() - to
print("The time interval is %f s." %td)