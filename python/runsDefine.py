#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:27:20 2020

@author: mccikpc2
"""
set1=1
if set1==1:
    runToDo = [['t_ctop=258.','t_ctop=230.'], \
               ['bam_nmlfile=\'pamm/bam/namelist.in\'',\
                    'bam_nmlfile=\'python/namelists/namelist.bam.change.in\''], \
               ['hm_flag=.true.','hm_flag=.false.'], \
               ['wr_flag=.true.','wr_flag=.false.'], \
               ['rm_flag=.true.','rm_flag=.false.'], \
               ['ice_flag=.true.','ice_flag=.false.'], \
                   ]
    columns1=['t','aer','hm','wr','rm','ice']

elif set1==2:
    runToDo = [['num_drop=1000.e6','num_drop=200.e6'], \
               ['rm_flag=.true.','rm_flag=.false.'], \
               ['hm_flag=.true.','hm_flag=.false.'], \
               ['mode1_ice_flag=0','mode1_ice_flag=1'], \
               ['mode2_ice_flag=0','mode2_ice_flag=1'], \
               ['coll_breakup_flag1=0','coll_breakup_flag1=2'], \
                   ]
    columns1=['num_c','rm','hm','m1','m2','br']
    

outputDir='/tmp'