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
"""
Problem 1: Type 1a Supernovae
"""
file=open("data/SN_z_mV.txt","r")
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


def dist_mod(m_V,MV):
    y=m_V-MV
    return y

MV=-19.6
distmod=dist_mod(m_V,MV)

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


file=open("data/defaults.dat","r")
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


file2=open("data/0.01.dat","r")
lines2=file2.readlines()
l2=[]
TT2=[]
EE2=[]
TE2=[]
for x in lines2:
    l2.append(float(x.split()[0]))
    TT2.append(float(x.split()[1]))
    EE2.append(float(x.split()[2]))
    TE2.append(float(x.split()[3]))
file2.close()

file3=open("data/0.1.dat","r")
lines3=file3.readlines()
l3=[]
TT3=[]
EE3=[]
TE3=[]
for x in lines3:
    l3.append(float(x.split()[0]))
    TT3.append(float(x.split()[1]))
    EE3.append(float(x.split()[2]))
    TE3.append(float(x.split()[3]))
file3.close()

file4=open("data/0.05.dat","r")
lines4=file4.readlines()
l4=[]
TT4=[]
EE4=[]
TE4=[]
for x in lines4:
    l4.append(float(x.split()[0]))
    TT4.append(float(x.split()[1]))
    EE4.append(float(x.split()[2]))
    TE4.append(float(x.split()[3]))
file4.close()

plt.figure(5)
plt.plot(l,TT,label='$\Omega_b h^2=0.0226$(default)')
plt.plot(l2,TT2,label='$\Omega_b h^2=0.01$')
plt.plot(l3,TT3,label='$\Omega_b h^2=0.1$')
plt.plot(l4,TT4,label='$\Omega_b h^2=0.05$')
plt.xlabel('l')
plt.ylabel('TT')
plt.legend()


plt.figure(6)
plt.plot(l,EE,label='$\Omega_b h^2=0.0226$(default)')
plt.plot(l2,EE2,label='$\Omega_b h^2=0.01$')
plt.plot(l3,EE3,label='$\Omega_b h^2=0.1$')
plt.plot(l4,EE4,label='$\Omega_b h^2=0.05$')
plt.xlabel('l')
plt.ylabel('EE')
plt.legend()


plt.figure(7)
plt.plot(l,TE,label='$\Omega_b h^2=0.0226$(default)')
plt.plot(l2,TE2,label='$\Omega_b h^2=0.01$')
plt.plot(l3,TE3,label='$\Omega_b h^2=0.1$')
plt.plot(l4,TE4,label='$\Omega_b h^2=0.05$')
plt.xlabel('l')
plt.ylabel('TE')
plt.legend()



file5=open("data/c_0.05.dat","r")
lines5=file5.readlines()
l5=[]
TT5=[]
EE5=[]
TE5=[]
for x in lines5:
    l5.append(float(x.split()[0]))
    TT5.append(float(x.split()[1]))
    EE5.append(float(x.split()[2]))
    TE5.append(float(x.split()[3]))
file5.close()

file6=open("data/c_0.15.dat","r")
lines6=file6.readlines()
l6=[]
TT6=[]
EE6=[]
TE6=[]
for x in lines6:
    l6.append(float(x.split()[0]))
    TT6.append(float(x.split()[1]))
    EE6.append(float(x.split()[2]))
    TE6.append(float(x.split()[3]))
file6.close()

file7=open("data/c_0.2.dat","r")
lines7=file7.readlines()
l7=[]
TT7=[]
EE7=[]
TE7=[]
for x in lines7:
    l7.append(float(x.split()[0]))
    TT7.append(float(x.split()[1]))
    EE7.append(float(x.split()[2]))
    TE7.append(float(x.split()[3]))
file7.close()

plt.figure(8)
plt.plot(l,TT,label='$\Omega_c h^2=0.112$(default)')
plt.plot(l5,TT5,label='$\Omega_c h^2=0.05$')
plt.plot(l6,TT6,label='$\Omega_c h^2=0.15$')
plt.plot(l7,TT7,label='$\Omega_c h^2=0.2$')
plt.xlabel('l')
plt.ylabel('TT')
plt.legend()


plt.figure(9)
plt.plot(l,EE,label='$\Omega_c h^2=0.112$(default)')
plt.plot(l5,EE5,label='$\Omega_c h^2=0.05$')
plt.plot(l6,EE6,label='$\Omega_c h^2=0.15$')
plt.plot(l7,EE7,label='$\Omega_c h^2=0.2$')
plt.xlabel('l')
plt.ylabel('EE')
plt.legend()


plt.figure(10)
plt.plot(l,TE,label='$\Omega_c h^2=0.112$(default)')
plt.plot(l5,TE5,label='$\Omega_c h^2=0.05$')
plt.plot(l6,TE6,label='$\Omega_c h^2=0.15$')
plt.plot(l7,TE7,label='$\Omega_c h^2=0.2$')
plt.xlabel('l')
plt.ylabel('TE')
plt.legend()


plt.show()
