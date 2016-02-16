# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:09:56 2016

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:43:08 2016

@author: user
"""

import numpy as np
from scipy.optimize import leastsq


def linear(p,x):
    return p[0]*x+p[1]


def errorfunc(p,x,z):
    return linear(p,x)-z

def lif(x,y) :
    n = x.size    
    a = (n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)
    b = (np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
    p = np.array([a, b], dtype=np.float)



    solp, ier = leastsq(errorfunc, 
                    p, 
                    args=(x,y),
                    Dfun=None,
                    full_output=False,
                    ftol=1e-9,
                    xtol=1e-9,
                    maxfev=100000,
                    epsfcn=1e-10,
                    factor=0.1)

    y_fitting = linear(solp,x)
    x = np.append(x,["coeffcient of x","constant"])
    y_fitting = np.append(y_fitting,solp)
    return x, y_fitting