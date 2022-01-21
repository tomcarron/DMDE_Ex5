import numpy as np
import astropy
import astropy.constants as const
import astropy.units as u
import matplotlib.pyplot as plt
from astropy.cosmology import Planck18_arXiv_v2 as P18
from astropy.cosmology import FlatwCDM
from astropy.cosmology import w0wzCDM
from astropy.cosmology import wCDM
import pandas as pd

'''
Script for DMDE exercise 5 by Tom Carron
'''
print("What kind of Dr was Dr pepper?")
print("A fizzician")
"""
Problem 1: Type 1a Supernovae
"""
file=open("SN_z_mV.txt","r")
lines=file.readlines()
name=[]
z=[]
m_V=[]
for x in lines[1:]:
    name.append(x.split('\t')[0])
    z.append(float(x.split('\t')[1]))
    m_V.append(float(x.split('\t')[2]))
file.close()

z=np.array(z)
m_V=np.array(m_V)

'''
a) Assuming the absolute magnitude of a Type Ia supernova is MV = −19.6, plot the observed distance modulus
of all the SNIa as a function of redshift.
'''

def dist_mod(m_V,MV):
    y=m_V-MV
    return y

MV=-19.6
distmod=dist_mod(m_V,MV)


'''
b) Choose at least three different combinations of cosmological parameters and plot the
distance moduli for each of these cosmologies on top of the previous plot. Python users
may find the astropy.cosmology package useful here.
c) Explain what you see in your plot
'''
z2=np.linspace(1e-2,1.4,1000)
#Set a comsology and then use cosmo.distmod(z)
#Planck18
variable=w0wzCDM(H0=67,Om0=0.3,Ode0=0.7, w0=-0.9, wz=0.5)
node=FlatwCDM(H0=67,Om0=1.0)
print(node.Ode0)


plt.figure(0)
plt.scatter(z,distmod,s=1)
plt.plot(z2,P18.distmod(z2),'--',color='red',label='Planck 2018')
plt.plot(z2,variable.distmod(z2),'--',color="green",label="Variable DE")
plt.plot(z2,node.distmod(z2),'--',color="orange",label="No DE")
plt.xlabel('$z$')
plt.ylabel('$(m_V - M_V)$')
plt.legend()

'''
Problem 2: The CMB
'''
'''
a) Download the data (Scalar Output) and plot T T, EE, and T E on a single plot with the
multipole moment l on the x-axis. Note that the columns in the downloaded .dat file
correspond to l, T T, EE and T E respectively. Make sure to note the units of power.
'''

file=open("defaults.dat","r")
lines=file.readlines()
l=[]
TT=[]
EE=[]
TE=[]
for x in lines:
    l.append(float(x.split()[0]))
    TT.append(float(x.split()[1]))
    EE.append(float(x.split()[2]))
    TE.append(float(x.split()[3]))
file.close()
l=np.array(l)
TT=np.array(TT)
EE=np.array(EE)
TE=np.array(TE)

plt.figure(1)
plt.plot(l,TT,label='TT')
plt.plot(l,EE,label='EE')
plt.plot(l,TE,label='TE')
plt.xlabel('l')
plt.ylabel('TT/EE/TE')
plt.legend()

'''
With our defaults, plot the temperature and polarization power spectra on their own
plots.
'''
plt.figure(2)
plt.plot(l,TT,label='TT')
plt.xlabel('l')
plt.ylabel('TT')
plt.legend()

plt.figure(3)
plt.plot(l,EE,label='EE')
plt.xlabel('l')
plt.ylabel('EE')
plt.legend()

plt.figure(4)
plt.plot(l,TE,label='TE')
plt.xlabel('l')
plt.ylabel('TE')
plt.legend()







plt.show()
