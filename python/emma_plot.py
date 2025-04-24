# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:35:33 2020

@author: mccikpc2
"""

from netCDF4 import Dataset
import numpy as np
from matplotlib import rc
#rc('font',family='serif')
#rc('text',usetex = True)
from svp import svp as svp
import matplotlib as mpl
import matplotlib
mpl.use('agg')

import os
import getpass

import matplotlib.pyplot as plt
#import pylab as plt

username=getpass.getuser()

def plot_model_run(fileName1):
    
    outputDir='/tmp/' + username + '/' 
    fileName=outputDir + fileName1
    
    nc=Dataset(fileName)
    
    time=nc['time'][:]
    
    plt.plot(time/60,np.cumsum(nc['precip'][:,0,0],axis=0)*10/3600.)
    #plt.plot(time/60,nc['precip'][:,0,0])
    plt.xlabel('time (mins)')
    #plt.ylabel('Precipitation (mm hr$^{-1}$)')
    plt.ylabel('Acc. Precipitation (mm)')
    
    
    nc.close()
    
    
if __name__=="__main__":
    fileNames=['output006.nc','output007.nc','output004.nc','output005.nc','output002.nc','output003.nc','output000.nc','output001.nc']
    leg1=['shallow, clean','shallow, clean, GCS','shallow, polluted','shallow, polluted, GCS','deep, clean','deep, clean, GCS','deep, polluted','deep, polluted, GCS']
    fig=plt.figure()

    for i in range(len(fileNames)):
        plot_model_run(fileNames[i])

    plt.legend(leg1)
    fig.savefig('/tmp/' + username + '/emma_plot.png',format='png')

