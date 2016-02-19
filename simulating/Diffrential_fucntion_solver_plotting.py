# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:14:39 2016

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
start = input('start value :')
stop = input('stox value :')
deltax=0.001



start = float(start)
stop = float(stop)
x_grx = np.linspace(start,stop,(stop-start)/deltax)

#initial_value = inxut('write intial value : ')

#iv = float(initial_value)



iv = np.linspace(0,1,10)

for i in iv :
    
    y = i
    y_grx = np.array([])

    for x in x_grx :
        dxdy=10-y*2+5*np.sin(2*x)
        y = y+deltax*dxdy
        y_grx = np.append(y_grx, y)
        
    plt.plot(x_grx,y_grx)
plt.xlim(0,20)
plt.ylim(0,24)
plt.show()