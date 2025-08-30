# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from tikzplotlib import save as tikz_save


def wave(t, w, phi=0):
    return -np.sin( w*t + phi)

##############################
# # Battements
w1    = 440
w2    = 460
t_end = 450/(w1+w2)

w3 = (w1+w2)/2
w4 = (w2-w1)/2

t = np.linspace( 0,t_end,500 ) 

plt.figure(figsize=(9,6))
plt.plot( t, wave(t,w1), label='w1=%.1f Hz'%(w1) )
plt.plot( t, wave(t,w2), label='w2=%.1f Hz'%(w2) )
plt.plot( t, wave(t,w1)+wave(t,w2), label='w1+w2=%.1f Hz'%(w1+w2) )
plt.plot( t, 2*np.cos( w4*t ) , label='w4=(w2-w1)/2=%.1f Hz'%(w4) )
plt.grid()
plt.legend()
plt.title('Battement (sin(w1*t) + sin(w2*t) = 2*sin(w3)*cos(w4))')
plt.xlabel('Time (s)')

tikz_save('Battement.tex')

###############################
# # The harmonic series

w0 = 440
T0 = 2*np.pi/w0

t2 = np.linspace( 0, 0.5*T0, 200 )

plt.figure(figsize=(10,5))
plt.plot( t2/T0, wave(t2, w0), label='1*w0 (unison)' )
plt.plot( t2/T0, 1/2*wave(t2, 2*w0), label='%i*w0 (octave)'%(2) )
plt.plot( t2/T0, 1/3*wave(t2, 3*w0), label='%i*w0 (P5)'%(3) )
plt.plot( t2/T0, 1/4*wave(t2, 4*w0), label='%i*w0 (2x octave)'%(4) )
plt.plot( t2/T0, 1/5*wave(t2, 5*w0), label='%i*w0 (M3)'%(5) )
plt.plot( t2/T0, 1/6*wave(t2, 6*w0), label='%i*w0 (P5)'%(6) )
plt.plot( t2/T0, 1/7*wave(t2, 7*w0), label='%i*w0 (m7)'%(7) )
plt.plot( t2/T0, 1/8*wave(t2, 8*w0), label='%i*w0 (3x octave)'%(8) )
plt.grid()
plt.legend(loc=0)
plt.title('The harmonic series ')
plt.xlabel('Fraction of the period')

tikz_save('Harmonics.tex')































