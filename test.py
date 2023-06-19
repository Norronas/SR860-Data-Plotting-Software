import math
import cmath
import sympy as smp
from scipy.integrate import quad


def complex_quadrature(func, a, b, **kwargs):
    """Comes from https://stackoverflow.com/questions/5965583/use-scipy-integrate-quad-to-integrate-complex-numbers 
        but modified by me
        Allows complex integrals to be calculated by separating the real from the imaginary
    """
    def real_func(x):
        real_tmp = func(x)
        return real_tmp.real
    def imag_func(x):
        imag_tmp = func(x)
        return imag_tmp.imag
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return(complex(real_integral[0] , imag_integral[0]))



nu = smp.symbols('nu', real=True)
smp.init_printing()

freq = 10000
frequency_list = []
real_result_list = []
imag_result_list = []
decade_mult = 0.001 
alpha1 = 1
alpha2 = 1
omega = (2*cmath.pi*freq)
prms = 20
constante = (-prms/(cmath.pi*1))             


B1 = lambda nu : (cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))
B2 = lambda nu : (cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))
phi1 = lambda nu : B1(nu) * 1
phi2 = lambda nu : B2(nu) * complex(1,0)
A2 = lambda nu : (-cmath.tanh(B2(nu)*1))
var1 = lambda nu : (((1*A2(nu)*B2(nu))/(1*B1(nu)))-cmath.tanh(phi1(nu)))
var2 = lambda nu : (1*A2(nu)*B2(nu)*cmath.tanh(phi1(nu))/(1*B1(nu)))
A1 = lambda nu : (var1(nu)/(1-var2(nu)))
fonction = lambda nu : (((cmath.sin(nu*1))**2)/(((nu*1)**2)*B1(nu)*A1(nu)))

result = complex_quadrature(fonction, 0, 1000000)
print(result)
