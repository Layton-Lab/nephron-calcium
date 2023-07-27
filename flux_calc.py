import os
import matplotlib.pyplot as plt
import numpy as np


fpath1 = 'Male_rat_normal_0.5'
fpath2 = 'Male_rat_normal_1.25'
fpath3 = 'Male_rat_normal_2.0'

segment = 'cTAL'
sex = 'male'
species = 'rat'
supjux = 'sup'

diam = 0.0020
length = 0.2


fname1 = fpath1+'/'+sex+'_'+species+'_'+segment+'_paracellular_Mg_'+supjux+'.txt'
y1=np.loadtxt(fname1, delimiter = '\n', unpack = True)
data1 = y1 * diam
flux_Ca1 = sum(data1)

fname2 = fpath2+'/'+sex+'_'+species+'_'+segment+'_paracellular_Mg_'+supjux+'.txt'
y2=np.loadtxt(fname2, delimiter = '\n', unpack = True)
data2 = y2 * diam
flux_Ca2 = sum(data2)

fname3 = fpath3+'/'+sex+'_'+species+'_'+segment+'_paracellular_Mg_'+supjux+'.txt'
y3=np.loadtxt(fname3, delimiter = '\n', unpack = True)
data3 = y3 * diam
flux_Ca3 = sum(data3)

print(flux_Ca1, flux_Ca2, flux_Ca3)