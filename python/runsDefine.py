#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:27:20 2020

@author: mccikpc2
"""

runToDo = [['t_ctop=258.','t_ctop=230.'], \
           ['bam_nmlfile=\'pamm/bam/namelist.in\'',\
                'bam_nmlfile=\'pamm/bam/namelist.change.in\''], \
           ['hm_flag=.true.','hm_flag=.false.'], \
           ['wr_flag=.true.','wr_flag=.false.'], \
           ['rm_flag=.true.','rm_flag=.false.'], \
           ['ice_flag=.true.','ice_flag=.false.'], \
               ]
columns1=['t','aer','hm','wr','rm','ice']
    

outputDir='/tmp'