# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:01:10 2016

@author: user
"""

import numpy as np
from scipy.optimize import leastsq
from numpy.linalg import inv


def quadratic(p,x):
    return p[0]*x**2+p[1]*x+p[2]


def errorfunc(p,x,z):
    return quadratic(p,x)-z

def qudf(x,y) :
    n = x.size
    i = np.sum(y)
    j = np.sum(x*y)
    k = np.sum((x**2)*y)
    m = np.sum(x)
    l = np.sum(x**2)
    o = np.sum(x**3)
    h = np.sum(x**4)
    A = np.array([[n,m,l],[m,l,o],[l,o,h]])
    B = np.array([i,j,k])
    A_inv = inv(A)
    X = np.dot(A_inv,B)
    a = X[0]
    b = X[1]
    c = X[2]
    p = np.array([a,b,c], dtype=np.float)



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

    y_fitting = quadratic(solp,x)
    x = np.append(x, ["coefficient of x^2","coefficeint of x","constant"])
    y_fitting = np.append(y,solp)
    return x, y_fitting