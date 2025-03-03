#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:27:20 2020

@author: mccikpc2
"""
set1=1
if set1==1:
    runToDo = [['t_ctop=220.','t_ctop=260.'], \
               [['bam_nmlfile=\'pamm/bam/namelist.in\'','num_drop=1006476818.2386227'],\
                    ['bam_nmlfile=\'python/namelists/namelist.bam.change.in\'','num_drop=817145878.67251050']], \
 	       ['num_ice=1.','num_ice=10.']
               ]
    columns1=['t','aer','num_ice']

elif set1==2:
    runToDo = [['num_drop=1006476818.2386227','num_drop=200.e6'], \
               ['rm_flag=.true.','rm_flag=.false.'], \
               ['hm_flag=.true.','hm_flag=.false.'], \
               ['mode1_ice_flag=0','mode1_ice_flag=1'], \
               ['mode2_ice_flag=0','mode2_ice_flag=1'], \
               ['coll_breakup_flag1=0','coll_breakup_flag1=2'], \
                   ]
    columns1=['num_c','rm','hm','m1','m2','br']
    

outputDir='/tmp'

#!elif set1==3:
#!     runToDo = [['t_ctop=238.','t_ctop=198.'],\
