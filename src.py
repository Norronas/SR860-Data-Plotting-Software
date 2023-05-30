import cmath
import scipy as sp
import sympy as smp
import numpy as np
from scipy.integrate import quad

#Comes from https://stackoverflow.com/questions/5965583/use-scipy-integrate-quad-to-integrate-complex-numbers
def complex_quadrature(func, a, b, **kwargs):
    def real_func(x):
        return np.real(func(x))
    def imag_func(x):
        return np.imag(func(x))
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return (real_integral[0] + 1j*imag_integral[0], real_integral[1:], imag_integral[1:])

#Parameter to integrate
nu = smp.symbols('nu', real=True)

#Parameters
R = 11.212 #Resistance
I = 0.028907 #Courant 
l = 0.0025 #Longueur de la ligne
prms = (R * I**2)/l
b = 0.000034/2
k = 0.297
rho = 1350
cp=1300

#Frequency to change
f = 10

#Equations
alpha = (k/(rho * cp)) 
q = cmath.sqrt(( j * 4 * cmath.pi * f)/alpha) 
f = lambda nu: (prms/(np.pi*k))*((cmath.sin(nu*b)**2)/(((nu*b)**2)*(cmath.sqrt(nu**2 + q**2))))



print("alpha :" + str(alpha))
print("q :" + str(q))
print(complex_quadrature(f, 0 , 10000000))
