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

def plot_model_run():
    u=2.5 # m/s
    # create a patch
    tau=6000.
    rt=tau
    t=np.linspace(0,rt,100)
    hill=tau*0.6/(2.*np.pi)*(1.-np.cos(2.*np.pi/tau*t))/1000.
    t=(t+10)*u/1000.
    t=np.append(t,t[::-1])
    hill=np.append(hill,np.zeros((len(hill),1)))
    l1=len(t)
    pgon=np.zeros((l1,2))
    pgon[:,0]=t
    pgon[:,1]=hill    
    pgon1=plt.Polygon(pgon,color='r',alpha=1)
    pgon2=plt.Polygon(pgon,color='r',alpha=1)
    pgon3=plt.Polygon(pgon,color='r',alpha=1)
    pgon4=plt.Polygon(pgon,color='r',alpha=1)
    
    outputDir='/tmp/' + username + '/' 
    fileName=outputDir + 'output.nc'
    
    nc=Dataset(fileName)
    
    time=nc['time'][:]
    z=nc['z'][:]+3000
    q=nc['q'][:,:,:]
    temp=nc['t'][:]
    theta=nc['theta'][:]
    p1=nc['p'][:]
    temp=theta*(p1/100000.)**(287/1005)
    
    m1=np.max(q[0,:,20]/1.e6)
    #plt.ion()
    fig=plt.figure(figsize=(12,6))     
    ax=plt.subplot(221)
    plt.pcolormesh(time/60,z/1000.,q[:,:,20].T/1.e6)
    plt.xlabel('time (mins)')
    plt.ylabel('z (km)')
    plt.clim((0,m1))
    plt.text(0.1,0.9,'(a) CDNC',color='white',transform=ax.transAxes)
    cbar=plt.colorbar()
    cbar.set_label('number of cloud drops (cm$^{-3}$)')
    #ax.add_patch(pgon1)
    
    ax=plt.subplot(222)
    plt.pcolormesh(time/60,z/1000.,q[:,:,21].T*1000.)
    plt.xlabel('time (mins)')
    plt.ylabel('z (km)')
    plt.text(0.1,0.9,'(b) $q_c$',color='white',transform=ax.transAxes)
    cbar=plt.colorbar()
    cbar.set_label('mass of cloud drops (g kg$^{-1}$)')
    #ax.add_patch(pgon2)
    
    ax=plt.subplot(223)
    plt.pcolormesh(time/60,z/1000.,q[:,:,32].T*1000.)
#     plt.clim((0,0.1))
    plt.xlabel('time (mins)')
    plt.ylabel('z (km)')
    plt.text(0.1,0.9,'(c) $q_r$',color='white',transform=ax.transAxes)
    cbar=plt.colorbar()
    cbar.set_label('mass of rain drops (g kg$^{-1}$)')
    #ax.add_patch(pgon3)
    
    (r,c,p)=np.shape(q)
    if(p>30):
        ax=plt.subplot(224)
        plt.pcolormesh(time/60,z/1000.,q[:,:,42].T/1000.,norm=matplotlib.colors.LogNorm())
        plt.xlabel('time (mins)')
        plt.ylabel('z k(m)')
        plt.text(0.1,0.9,'(d) $N_{ice}$',color='white',transform=ax.transAxes)
        cbar=plt.colorbar()
        plt.contour(time/60,z/1000.,temp.T,[268.15,273.15],colors='m')
    #     plt.clim((0,1000))
        cbar.set_label('number of ice crystals (L$^{-1}$)')
    #ax.add_patch(pgon4)
    

    
#     fig2=plt.figure()
#     plt.plot(time/60,np.cumsum(nc['precip'][:,0,0],axis=0)*10/3600.)
#     plt.xlabel('time (mins)')
#     plt.ylabel('Precipitation (mm hr$^{-1}$)')
#     plt.ylabel('Acc. Precipitation (mm)')
#     
#     fig2.savefig('/tmp/' + username + '/scm_plot2.png',format='png')


    
    nc.close()
    #plt.show()
    
    fig.savefig('/tmp/' + username + '/scm_plot.png',format='png')
    
if __name__=="__main__":
    plot_model_run()

