import numpy as np 
from scipy.optimize import leastsq
 
def lorentzian(x,p):
    numerator =  (p[0]**2 )
    denominator = ( x - (p[1]) )**2 + p[0]**2
    y = p[2]*(numerator/denominator)
    return y
 
def gaussian(x,p):
    c = p[0] / 2 / np.sqrt(2*np.log(2))
    numerator = (x-p[1])**2
    denominator = 2*c**2
    y = p[2]*np.exp(-numerator/denominator)
    return y
 
def residuals(p,y,x):
    err = y - lorentzian(x,p)
    return err
 
def local_fit(x, y):
    y_bg=y.min()
    p = [(x.max()-x.min())/2, (x.max()-x.min())/2+x.min() , x.max()-x.min()]
    # [fwhm, peak center, intensity] #
    pbest = leastsq(residuals, p, args=(y-y_bg,x), full_output=1)
    best_parameters = pbest[0]
    best_parameters[0] *= 2 
    fit = lorentzian(x,best_parameters) + y_bg
    return best_parameters,  x, fit,
 
def lf(x,y):
    
    line = np.abs(y)
    x_orig = x
    fit_result = local_fit(x_orig, line[0:])
    x_fit = fit_result[1]
    y_fit = fit_result[2]
    x_fit = np.append(x_fit,["FWHM","Center","Amplitude"])
    y_fit = np.append(y_fit,fit_result[0])
    return x_fit, y_fit
