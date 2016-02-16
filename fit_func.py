# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:43:08 2016

@author: user
"""

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt


def lorentz(p,x):
    return (np.exp(-(x-p[0])**2/(2*p[1])))/((np.sqrt(p[1]*2*np.pi)))*(x[1]-x[0])


def errorfunc(p,x,z):
        return lorentz(p,x)-z

Data =np.loadtxt("C:\\Users\\user\\Desktop\\scan\\Scan01.dat")
Data = np.transpose(Data)

x =Data[0]
y= Data[1]
y = np.abs(y)/np.sum(np.abs(y))
mean = np.sum(x*y)
var = np.sum((x**2)*y)-(mean**2)
p = np.array([mean, var], dtype=np.float)



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

y_fitting = lorentz(solp,x)*np.sum(np.abs(Data[1]))
y_fit = lorentz(p,x)*np.sum((np.abs(Data[1])))

plt.plot(x,np.abs(Data[1]))
plt.plot(x,y_fitting)
plt.plot(x,y_fit)
plt.show()