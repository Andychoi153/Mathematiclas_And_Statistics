# -*- coding: utf-8 -*-
"""
Spyder Editor Andychoi

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

def pac(k) :    
    j=1
    for i in range(k+1) :
        if i != 0 :
            j *= i
            
    return j

        
    
def pactorial(N,s) :
    k = pac(N)/(pac(N//2-s)*pac(N//2+s))
    return k

def gausian(N,s):
    e = 2.72
    pi = 3.14
    k = ((2/(pi*N))**(1/2))*(2**N)*(e**(-2*s*s/N))
    return k
    
G = np.array([])
P = np.array([])

n = input("표본들의 수를 써주세요 : \t")
N = int(n)

for i in range(N//2) :
    P = np.append(P,pactorial(N,-N//2+i))
    G = np.append(G,gausian(N,-N//2+i))    

for i in range(N//2+1) :
    P = np.append(P,pactorial(N,i))
    G = np.append(G,gausian(N,i))
    
x = np.linspace(-N//2,N//2,N+1)
plt.plot(x,P)
plt.plot(x,G)

plt.show()