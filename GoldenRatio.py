#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:20:42 2021

@author: nate_mac
"""

import numpy as np
from matplotlib import pyplot as plt

def fib(n):
    l = np.arange(n)
    for i in range(n):
        if i == 0 or i == 1:
            l[i] = i
        else:
            l[i] = l[i-1]+l[i-2]
    return(l)

#performing the function with only array math
def ratioMatrix(array):
    new = np.roll(array,1)
    new[0] = 0
    #print(array)
    #print(new)
    out = np.divide(array[2:], new[2:])
    return(out)

#performing the function with a loop (not utilized)
def ratioLoop(array):
    r = []
    #print(len(array))
    for i in range(len(array)):
        if i<= 1:
            r.append(i)
        else:
            #print(array[i]/array[(i-1)])
            ratio = array[i]/array[(i-1)]
            r.append(ratio)
    r = np.array(r)
    return(r)
    
n = 25   

seq = fib(n)
ratio = ratioMatrix(seq)
reps = np.arange(2,n)

#1.618033 is the true golden ratio 
#My code does not plot the first two numbers, the /0 erorr was causing problems
#As such the plot begins from term 3  
#It takes 8 iterations for 3 digits of accuracy (1.61...)
#Then 14 iterations for 5 digits of accuracy (1.6180...) 
#Depending on needed precision, between 10-20 terms needed to converge true value

plt.plot(reps,ratio, '--r')

plt.title("Fibinauci Approximation") 
plt.xlabel("Iterations (n)") 
plt.ylabel("Ratio (F=Fn / Fn - 1)") 



