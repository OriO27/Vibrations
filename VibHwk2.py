"""
OOrtiz
29JUNE20
ME 4110
Inspired by Prof Ploen MATLAB script
Undamped Vibration
"""

import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def hwk2_1():
    #Given
    k = 6000            #Stiffness [N/m]
    m = 10              #Mass [kg]
    w_n = np.sqrt(k/m)  #Natural Frequency [1/s]    
    
    #Initial Conditions
    X_0 = 0.02          #I.C. @ X=0 [m]
    X_dot_0 = -3        #I.C @V=0 [m/s]
    
    lamb = 0            #Lamba from characteristic EQ From table     
    
    #For Case III
    C1 = X_0                                #From table 
    C2 = (X_dot_0 - lamb * X_0 ) / w_n      #From Table
    A = np.sqrt(C1**2 + C2**2)              #Amplitude using Amp phase identity [m]

    theta = np.arctan2( C1, C2 )            #Phase angle
    T_ = 2* np.pi /w_n                      #Period
    #delay = theta / w_n                    #Time Delay
    #time = np.arange(0, 2*T_,0.01)         #Timestep arrange(start,stop,timestep) start @ t=0, stop at 2 Periods
    
    t = Symbol('t')                         #make 'symbol' for var
    
    #Displacement
    x_t = A * sin(w_n * t + theta)          #displacement eq
    #Velocity
    v_t = diff(x_t, t)                      #dx/dt function
    #Acceleration
    a_t = diff(v_t, t)                      #d^2x/dt^2


    E = 1/2 * k * A**2                      #Energy [J]
    print("Energy of the system: {:.1f} J".format(E))
    #Vibration Plot
    allplot = plot(x_t, v_t, a_t, (t,0,T_),title='Undamped Vibration'\
        ,xlabel='time (s)',ylabel='m | m/s | m/s^2',legend=True, show=False ) #plot(f1,f2,f3,(t,range),format**)
    allplot[0].line_color = 'r'         #Displacement Color 'red'
    allplot[1].line_color = 'g'         #Velocity Color 'green'
    allplot[2].line_color = 'b'         #Acceleration Color 'blue'
    allplot.show()

hwk2_1()

def hwk2_2():
    a_max = 50              #max acceleration [m/s^2]
    f = 30                  #Frequency [Hz]
    w_n = 2*np.pi * f       #Natural Frequency [rad/s]
    A = a_max/w_n**2        #Amplitude
    v_max = A * w_n         #max velocity [m/s]
    x_max = A               #max displacement [m]

    print("Maximum Displacement: {:.2e} m".format(x_max))
    print("Maximum Velocity: {:.3f} m/s".format(v_max))
    print("Maximum Acceleration: {:.1f} m/s^2".format(a_max))
    print("Narutal Frequency: {:.1f} rad/s".format(w_n))

hwk2_2()


