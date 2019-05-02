#### Max Factor

import time

to = time.time()

def show_max_factor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("The max factor of %d is %d." %(num,count))
            break
        count = count - 1
    else:
        print("%d is a prime number." % num)

num = int(input("Please input an integer.\n"))
show_max_factor(num)

td = time.time() - to
print("The time interval is %f s." %td)