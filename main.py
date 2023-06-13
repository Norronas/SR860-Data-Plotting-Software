import graphics
import cmath
#import scipy as sp
import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad  
import pyvisa

MAX_INTEGRATE = 100000
MIN_FREQUECY = 0.001
MAX_FREQUENCY = 1000000
MAX_LIST = 1000
DECADE = 10

'''Comes from https://stackoverflow.com/questions/5965583/use-scipy-integrate-quad-to-integrate-complex-numbers but modified by me'''
def complex_quadrature(func, a, b, **kwargs):
    def real_func(x):
        return np.real(func(x))
    def imag_func(x):
        return np.imag(func(x))
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return(complex(real_integral[0] , imag_integral[0]))


def point_calculation_layer1(R, I, l, b, k, rho, cp, T, window):
    freq = MIN_FREQUECY
    frequency_list = []
    real_result_list = []
    imag_result_list = []
    decade_mult = 0.001 #1
    prms = (R * I**2)/l
    constante = (-prms/(cmath.pi*k))
    alpha = (k/(rho * cp)) 
    #q = cmath.sqrt(( complex(0,1) * 4 * cmath.pi * freq)/alpha)
    while(freq <= MAX_FREQUENCY):
        for i in range (1,DECADE):
            
            if (int(graphics.Window.get_value_mode(window)) == 0):
                A1 = (-1)
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

            frequency_list.append(np.log(4*np.pi*freq))                                                 #Transformation Hz to ln(2w)
            real_result_list.append(1000*(0.5*R*I*(float(window.tcr_entry.get()))*(np.real(result))))   #Transformation delta(T) to mV
            imag_result_list.append(1000*(0.5*R*I*(float(window.tcr_entry.get()))*(np.imag(result))))   #Transformation delta(T) to mV
            freq = (i+1) * decade_mult
        decade_mult *= 10
    fmin = ((25*alpha) / (4*cmath.pi*(T**2)))
    fmax = (alpha / (100*cmath.pi*(b**2)))
    graphics.Window.freq_change_label_value(window, fmin, fmax)
    graphics.Window.canvas_draw_freq(window, np.log(4*np.pi*fmin), np.log(4*np.pi*fmax))
    graphics.Window.canvas_draw(window, frequency_list, real_result_list, imag_result_list)



def point_calculation_layer2(R, I, l, b, k1, rho1, cp1, T1, k2, rho2, cp2, T2, window):
    freq = MIN_FREQUECY
    frequency_list = []
    real_result_list = []
    imag_result_list = []
    decade_mult = 0.001 #1
    alpha1 = (k1/(rho1 * cp1))
    alpha2 = (k2/(rho2 * cp2)) 
    omega = (2*cmath.pi*freq)
    prms = (R * I**2)/l
    constante = (-prms/(cmath.pi*k1))             

    # B1 = lambda nu : (cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))
    # B2 = lambda nu : (cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))
    # phi1 = B1 * T1
    # phi2 = B2 * T2 
    # var1 = ((k2*A2*B2/(k1*B1))-cmath.tanh(phi1))
    # var2 = (k2*A2*B2*cmath.tanh(phi1)/(k1*B1))
    # A1 = (var1/(1-var2))
    # fonction = lambda nu : (((cmath.sin(nu*b))**2)/(((nu*b)**2)*B1*A1))
    while(freq <= MAX_FREQUENCY):
        for i in range (1,DECADE):
            if (int(graphics.Window.get_value_mode(window)) == 0):
                A2 = -1
                fonction = lambda nu : (((cmath.sin(nu*b))**2)/(((nu*b)**2)*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))*(((k2*A2*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))))-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1))) * T1))/(1-(k2*A2*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))*cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1))) * T1)/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))))))))
                # fonction = lambda nu : (((cmath.sin(nu*b))**2)/(((nu*b)**2)*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))*(((k2*A2*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))))-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1))) * T1))/(1-(k2*A2*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))*cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1))) * T1)/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))))))))
                result = constante * complex_quadrature(fonction, 0, MAX_INTEGRATE)
            if (int(graphics.Window.get_value_mode(window)) == 1):
                # A2 = lambda nu : (-cmath.tanh(B2*T2))
                fonction = lambda nu : (((cmath.sin(nu*b))**2)/(((nu*b)**2)*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))*(((k2*(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))*T2))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))))-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1))) * T1))/(1-(k2*(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))*T2))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))*cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1))) * T1)/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))))))))
                # fonction = lambda nu : (((cmath.sin(nu*b))**2)/(((nu*b)**2)*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))*(((k2*(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))*T2))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))))-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1))) * T1))/(1-(k2*(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))*T2))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))*cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1))) * T1)/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))))))))
                result = constante * complex_quadrature(fonction, 0, MAX_INTEGRATE)
            if (int(graphics.Window.get_value_mode(window)) == 2):
                # A2 = lambda nu : (-1/(-cmath.tanh(B2*T2)))
                fonction = lambda nu : (((cmath.sin(nu*b))**2)/(((nu*b)**2)*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))*(((k2*(-1/(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))*T2)))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))))-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1))) * T1))/(1-(k2*(-1/(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))*T2)))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha2)))*cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1))) * T1)/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*(2*cmath.pi*freq)/alpha1)))))))))
                # fonction = lambda nu : (((cmath.sin(nu*b))**2)/(((nu*b)**2)*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))*(((k2*(-1/(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))*T2)))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))))-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1))) * T1))/(1-(k2*(-1/(-cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))*T2)))*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha2)))*cmath.tanh((cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1))) * T1)/(k1*(cmath.sqrt((1*(nu**2))+(complex(0,1)*omega/alpha1)))))))))
                result = constante * complex_quadrature(fonction, 0, MAX_INTEGRATE)

            frequency_list.append(np.log(4*np.pi*freq))                                                 #Transformation Hz to ln(2w)
            real_result_list.append(1000*(0.5*R*I*(float(window.tcr_entry.get()))*(np.real(result))))   #Transformation delta(T) to mV
            imag_result_list.append(1000*(0.5*R*I*(float(window.tcr_entry.get()))*(np.imag(result))))   #Transformation delta(T) to mV
            freq = (i+1) * decade_mult
        decade_mult *= 10
    fmin = ((25*alpha1) / (4*cmath.pi*(T1**2)))
    fmax = (alpha1 / (100*cmath.pi*(b**2)))
    graphics.Window.freq_change_label_value(window, fmin, fmax)
    graphics.Window.canvas_draw_freq(window, np.log(4*np.pi*fmin), np.log(4*np.pi*fmax))
    graphics.Window.canvas_draw(window, frequency_list, real_result_list, imag_result_list)



def zero_verification(l, k, rho, cp, window):
    point_calculation_layer2(11.212, 0.028907, 0.0025, 0.000034/2, 0.297, 1350, 1300, 0.0004, 1.3, 2630, 680, 0.000001, window)
    # point_calculation_layer1(11.212, 0.028907, 0.0025, 0.000034/2, 0.297, 1350, 1300, 0.0004, window)
    if(l == "" or k == "" or rho == "" or cp == ""):
        graphics.Window.create_error_window(window, 2)
        return 0
    elif(float(l) == 0 or float(k) == 0 or float(rho) == 0 or float(cp) == 0):
        graphics.Window.create_error_window(window, 3)
        return 0
    else:
        if (int(graphics.Window.get_value_layer(window)) == 1):
            point_calculation_layer1(float(window.resistance_entry.get()),
                            float(window.current_entry.get()),
                            float(window.length_entry.get()),
                            float(window.width_entry.get())/2,
                            float(window.thermal_cond1_entry.get()),
                            float(window.densit1_entry.get()),
                            float(window.heat_capa1_entry.get()),
                            float(window.thickness1_entry.get()),
                            graphics.Window)
            
        elif (int(graphics.Window.get_value_layer(window)) == 2):
            point_calculation_layer2(float(window.resistance_entry.get()),
                            float(window.current_entry.get()),
                            float(window.length_entry.get()),
                            float(window.width_entry.get())/2,
                            float(window.thermal_cond1_entry.get()),
                            float(window.densit1_entry.get()),
                            float(window.heat_capa1_entry.get()),
                            float(window.thickness1_entry.get()),
                            float(window.thermal_cond2_entry.get()),
                            float(window.densit2_entry.get()),
                            float(window.heat_capa2_entry.get()),
                            float(window.thickness2_entry.get()),
                            graphics.Window)


def init_data_collect_lockin(window):
    try:
        lockin = pyvisa.RessourceManager().open_ressource() #Mettre le truc là
    except:
        graphics.Window.create_error_window(window, 1)
        return 0

def collect_data_lockin(window):
    return 0
    reel = sr860.ask("*OUTR? [0]\n")
    imag = sr860.ask("*OUTR? [1]\n")
    freq = sr860.ask("*OUTR? [2]\n")
    graphics.Window.canvas_draw_data_points(window, reel, imag, freq)




def main():
    nu = smp.symbols('nu', real=True)
    window = graphics.Window()
    init_data_collect_lockin(window)
    window.mainloop()

if __name__ == '__main__':
    main()
