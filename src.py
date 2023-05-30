import cmath
import scipy
from scipy.integrate import quad


def complex_quadrature(func, a, b, **kwargs):
    def real_func(x):
        return scipy.real(func(x))
    def imag_func(x):
        return scipy.imag(func(x))
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return (real_integral[0] + 1j*imag_integral[0], real_integral[1:], imag_integral[1:])


complexe = complex(0,0)
complexe += 1
complexe +=3j

k = 2
rho = 1
cp=1
f = 100
alpha = 1 
j = complex(0,1)
print("REEL : " + str(complexe))
print(complexe)

alpha = (k/rho * cp) #CALCUL EQUA 1.50
q = cmath.sqrt(( j * 4 * cmath.pi * f)/alpha) #CALCUL EQUA 1.50


print(alpha)
print(q)

