import time
import sys
import random

#need this to pad the animation
height = 48
width = 48

#the canvas we have to work with
screen1 = [['-']*width for i in range(height)]
screen2 = [['-']*width for i in range(height)]

a = '''
     __ __   ___   __ __  __  __ __    ___ 
    |  T  T /   \ |  T  TT  ||  T  |  /  _]
    |  |  |Y     Y|  |  |l_ ||  |  | /  [_ 
    |  ~  ||  O  ||  |  |  \l|  |  |Y    _]
    l___, ||     ||  :  |    l  :  !|   [_ 
    |     !l     !l     |     \   / |     T
    l____/  \___/  \__,_j      \_/  l_____j
     __    __   ___   ____   __  __  __    
    |  T__T  T /   \ |    \ |  T|  T|  T   
    |  |  |  |Y     Y|  _  Y|  ||  ||  |   
    |  |  |  ||  O  ||  |  ||__j|__j|__j   
    l  `  '  !|     ||  |  | __  __  __    
     \      / l     !|  |  ||  T|  T|  T   
      \_/\_/   \___/ l__j__jl__jl__jl__j   
'''

b = a.strip('\n').split('\n')

for j in range(height):
    for k in range(width):
        if j%2 == 0:
            if k%2 == 0:
                screen1[j][k] = '+'
        elif k%2 == 1:
            screen1[j][k] = '+'

for j in range(height):
    for k in range(width):
        if j%2 == 1:
            if k%2 == 0:
                screen2[j][k] = '+'
        elif k%2 == 1:
            screen2[j][k] = '+'

def randomizer(a,line):
    b = ['x'*48]
    for i,k in enumerate(a):
        if i > line:
            print("".join(b))
        else:
            print("".join(k))
def checker_print(i):
    if(i%2 == 0):
        print("\n".join("".join(i) for i in screen1[:48-25]))
    else:
        print("\n".join("".join(i) for i in screen2[:48-25]))
    randomizer(b,i)
    if(i%2 == 0):
        print("\n".join("".join(i) for i in screen1[25:]))
    else:
        print("\n".join("".join(i) for i in screen2[25:]))
    sys.stdout.flush()
                                 
for i in range(40):
    checker_print(i)
    time.sleep(0.2)
