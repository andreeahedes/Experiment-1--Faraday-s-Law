# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:22:08 2020

@author: ah920
"""

import matplotlib.pyplot as plt 
import numpy as np
from scipy import signal 

f=5*1e3#the frequnecy 
v_0=2#the amplitude of the signal 
N_s=52#the number of turns for the secondary coil
N_p=98#the number of turns for the primary coil
l_s=6*1e-2#length of the secondary coil
l_p=12.2*1e-2#lenght of the primary coil
S_p=np.pi*50**2*1e-6/4#area of the primary coil
S_s=np.pi*32**2*1e-6/4#area od the secondary coil
S_core=np.pi*10**2*1e-6/4
nu_0=4*np.pi*1e-7#magnetic permeability of void
k_core=1500#relative permeability of the core used (variable)
k_air=1.00000037#relative permeability of air
nu=((S_core/S_s)*k_core +(S_s-S_core)*k_air)*nu_0#permeability of the combined core
L_P=2*np.pi*f*nu*N_p*S_p/l_p# inductance of the primary coil
L_S=2*np.pi*f*nu*N_s*S_s/l_s# inductance of the secondary coil
n_p=N_p/l_p#number of turns per unit lenght for the primary coil
n_s=N_s/l_s#number of turns per unit lenght for the secondary coil
R=18#resistance used in the experiment, which was in series with the primary coil


t=np.linspace(0,10,100)


def X_l(f,L):# calculating the reactance for the primary coil
    return 2*np.pi*f*L

def sinusoidal(f,t):#sinusoidal signal for the voltage applied to the circuit
    return np.sin(2*np.pi*f*t)

def square(f,t):#square wave signal
    return signal.square(2*np.pi*f*t,0.5)

def triangle(f, t):#triangle wave signal
    return signal.sawtooth(2*np.pi*f*t,0.5)

def i_p(V_0,X_l,R):# function which calculates the peak value for the intesisty of the current through the primary coil
    return V_0/np.sqrt(R**2+X_l**2)

def i_s(Vp,ns, np,xl):# calculates the peak value for the current intesnity through the secondary coil
    Vs=ns*Vp/np
    return Vs/xl
    
def Faraday(V_form,v_0,f,N_s,N_p,t,xls):# as we don't know the inductance for the secondary coil for the used frequency, we put it as a variable 
    Ip=i_p(v_0,X_l(f,L_P),R)#calculating the value for the I peak in the primary coil
    Vp=2*np.pi*f*L_P*Ip#calculating the value for the V peak across the primary coil
    E_p=-Vp*np.gradient(V_form)# the produced voltage of the primary coil
    Is=i_s(Vp,n_s,n_p,xls)#we have the same procedure for the secondary coil
    Vs=2*np.pi*f*L_S*Is
    E_s=-Vs*np.gradient(V_form)
    plt.plot(t,E_p, label='Primary coil')
    plt.plot(t,E_s,label='Secondary Coil')
    plt.grid()
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage(s)')
    plt.show()
    

Faraday(sinusoidal(f,t),v_0,f,N_s,N_p,t,12e5)







