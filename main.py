import graphics
import cmath
#import scipy as sp
import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad  

MAX_INTEGRATE = 10000000
MIN_FREQUECY = 1
MAX_FREQUENCY = 1000000
MAX_LIST = 1000
DECADE = 10

#Comes from https://stackoverflow.com/questions/5965583/use-scipy-integrate-quad-to-integrate-complex-numbers but modified by me
def complex_quadrature(func, a, b, **kwargs):
    def real_func(x):
        return np.real(func(x))
    def imag_func(x):
        return np.imag(func(x))
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return(complex(real_integral[0] , imag_integral[0]))
    #return (real_integral[0] + 1j*imag_integral[0])
    #return (real_integral[0] + 1j*imag_integral[0], real_integral[1:], imag_integral[1:])


def point_calculation(R, I, l, b, k, rho, cp, T, window):
    print("1")
    # if(zero_verification(l, k, rho, cp, window) == 0):
    #     print("2")
    #     return
    freq = MIN_FREQUECY
    frequency_list = []
    real_result_list = []
    imag_result_list = []
    decade_mult = 1
    prms = (R * I**2)/l
    constante = (-prms/(cmath.pi*k))
    alpha = (k/(rho * cp)) 
    #q = cmath.sqrt(( complex(0,1) * 4 * cmath.pi * freq)/alpha)
    while(freq <= MAX_FREQUENCY):
        for i in range (1,DECADE):
            if (int(graphics.Window.get_value_mode(window)) == 0):
                A1 = -1
                fonction = lambda nu : ((1/(A1*(cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha)))))*((cmath.sin(nu*b)**2)/(b*nu)**2))
                result = constante * complex_quadrature(fonction, 0, MAX_INTEGRATE)
            if (int(graphics.Window.get_value_mode(window)) == 1):
                # A1 = (-cmath.tanh((cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha))) * T))
                fonction = lambda nu : ((1/((-cmath.tanh((cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha))) * T))*(cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha)))))*((cmath.sin(nu*b)**2)/(b*nu)**2))
                result = constante * complex_quadrature(fonction, 0, MAX_INTEGRATE)
            if (int(graphics.Window.get_value_mode(window)) == 2):
                # A1 = (-1/(cmath.tanh((cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha))) * T)))
                fonction = lambda nu : ((1/((-1/(cmath.tanh((cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha))) * T)))*(cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha)))))*((cmath.sin(nu*b)**2)/(b*nu)**2))
                result = constante * complex_quadrature(fonction, 0, MAX_INTEGRATE)
            #q = cmath.sqrt(( complex(0,1) * 4 * cmath.pi * freq)/alpha)
            #fonction = lambda nu: (prms/(np.pi*k))*((cmath.sin(nu*b)**2)/(((nu*b)**2)*(cmath.sqrt(nu**2 + q**2))))
            #result = complex_quadrature(fonction, 0 , MAX_INTEGRATE)
            frequency_list.append(np.log(4*np.pi*freq))
            real_result_list.append(np.real(result))
            imag_result_list.append(np.imag(result))
            freq = (i+1) * decade_mult
        decade_mult *= 10
        print(real_result_list)
    graphics.Window.modify_status(window, 1)
    graphics.Window.canvas_draw(window, frequency_list, real_result_list, imag_result_list)

def zero_verification(l, k, rho, cp, window):
    point_calculation(11.212, 0.028907, 0.0025, 0.000034/2, 0.297, 1350, 1300, 0.0004, window)
    if(l == "" or k == "" or rho == "" or cp == ""):
        graphics.Window.modify_status(window, 2)
        return 0
    elif(float(l) == 0 or float(k) == 0 or float(rho) == 0 or float(cp) == 0):
        graphics.Window.modify_status(window, 3)
        print("AIEIIIE")
        return 0
    else:
        point_calculation(float(window.resistance_entry.get()),
                        float(window.current_entry.get()),
                        float(window.length_entry.get()),
                        float(window.width_entry.get())/2,
                        float(window.thermal_cond_entry.get()),
                        float(window.density_entry.get()),
                        float(window.heat_capa_entry.get()),
                        float(window.thickness_entry.get()),
                        graphics.Window)

#Parameter to integrate

#Parameters
# R = 11.212 #Resistance
# I = 0.028907 #Courant 
# l = 0.0025 #Longueur de la ligne
# b = 0.000034/2
# k = 0.297
# rho = 1350
# cp=1300

#Frequency to change

#Equations
# prms = (R * I**2)/l
# alpha = (k/(rho * cp)) 
# q = cmath.sqrt(( complex(0,1) * 4 * cmath.pi * freq)/alpha) 
# fonction = lambda nu: (prms/(np.pi*k))*((cmath.sin(nu*b)**2)/(((nu*b)**2)*(cmath.sqrt(nu**2 + q**2))))

#fonction = lambda nu: (prms/(np.pi*k))*((cmath.sin(nu*b)**2)/(((nu*b)**2)*(cmath.sqrt(nu**2 + q**2))))


#AUTRE METHODE
# constante = (-prms/(cmath.pi*k))
# A1 = -1
# B1 = lambda nu : (cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha))) 
# fonction2 = lambda nu : ((1/(A1*(cmath.sqrt((nu**2)+((complex(0,1) * 4 * cmath.pi * freq)/alpha)))))*((cmath.sin(nu*b)**2)/(b*nu)**2)) #REMPLACER B1 PAR SA FONCTION 
# result = constante * complex_quadrature(fonction2, 0, MAX_INTEGRATE)
# print(result)

def main():
    nu = smp.symbols('nu', real=True)
    window = graphics.Window()
    window.mainloop()

if __name__ == '__main__':
    main()

#point_calculation(R,I,l,b,k,rho,cp, fonction)

#plot_result(frequency_list,real_result_list, imag_result_list)

