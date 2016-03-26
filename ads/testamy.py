#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys

#need this to pad the animation
height = 40
width = 40

#the canvas we have to work with
screen = [['-']*width for i in range(height)]

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
b='''













                                        
'''

def explode_move(screen, height,width, character_null, character_fun):
    temp = [['-']*width for i in range(height)]
    for i in range(height):
        for j in range(width):
            temp[i][j] = screen[i][j]
    
    for i in range(height):
        for j in range(width):
            if screen[i][j] == character_fun and i!= height-1 and j!= width-1:
                #temp[i][j] = character_null
                if i == height//2 and j == width//2:
                    #print("oh hey you are starting")
                    temp[min(height-1,i)][min(width-1,j+1)] = character_fun
                    temp[min(height-1,i+1)][min(width-1,j)] = character_fun
                    temp[min(height-1,i-1)][min(width-1,j)] = character_fun
                    temp[min(height-1,i)][min(width-1,j-1)] = character_fun
                elif i == height//2 and j < width//2:
                    #print("1")
                    temp[min(height-1,i+1)][min(width-1,j-1)] = character_fun
                    temp[min(height-1,i-1)][min(width-1,j-1)] = character_fun
                elif i == height//2 and j > width//2:
                    #print("2")
                    temp[min(height-1,i-1)][min(width-1,j+1)] = character_fun
                    temp[min(height-1,i+1)][min(width-1,j+1)] = character_fun
                elif j == width//2 and i < height//2:
                    #print("3")
                    temp[min(height-1,i-1)][min(width-1,j+1)] = character_fun
                    temp[min(height-1,i-1)][min(width-1,j-1)] = character_fun
                elif j == width//2 and i > height//2:
                    #print("4")
                    temp[min(height-1,i+1)][min(width-1,j-1)] = character_fun
                    temp[min(height-1,i+1)][min(width-1,j+1)] = character_fun
                elif i > height//2 and j > width//2:
                    #print("5")
                    temp[min(height-1,i)][min(width-1,j+1)] = character_fun
                    temp[min(height-1,i+1)][min(width-1,j)] = character_fun
                elif i > height//2:
                    #print("6")
                    temp[min(height-1,i+1)][min(width-1,j)] = character_fun
                    temp[min(height-1,i)][min(width-1,j-1)] = character_fun
                elif j > height//2:
                    #print("7")
                    temp[min(height-1,i)][min(width-1,j+1)] = character_fun
                    temp[min(height-1,i-1)][min(width-1,j)] = character_fun
                else:
                    #print("8")
                    temp[min(height-1,i)][min(width-1,j-1)] = character_fun
                    temp[min(height-1,i-1)][min(width-1,j)] = character_fun
    return temp

def explode_print(screen, flah):
    print("\n".join("".join(i) for i in screen[:48-25]))
    if(flah):
        print(a)
    else:
        print(b)
    print("\n".join("".join(i) for i in screen[25:]))
    sys.stdout.flush()

screen[height//2][width//2] = '+'
flah = True

for i in range(height//2+1):
    explode_print(screen, flah)
    if(flah == True):
        flah= False
    else:
        flah = True
    screen = explode_move(screen,height,width, '-', '+')
    time.sleep(0.2)
screen[height//2][width//2] = '-'
for i in range(height//2+1):
    explode_print(screen, flah)
    if(flah == True):
        flah= False
    else:
        flah = True
    screen = explode_move(screen,height,width, '+', '-')
    time.sleep(0.2)
