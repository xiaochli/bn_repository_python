# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 23:19:28 2016

@author: xiaocheng-mac
"""

import numpy as np
import os

networkFileName = "asia.bif"
nSample = 1000
sampleFileName = "asia.csv"

''' path is the path to the installation folder of gobnilp, please change it here! '''
path = '/Users/xiaocheng-mac/Desktop/grad4/courses/StrLr/gobnilp1.6.2'

'''sampling using sample.R'''
os.system("Rscript --vanilla sampling.R {} {} {}".format(networkFileName, nSample, sampleFileName))

''' structure learning by gobnlip''''
os.system(path+'/bin/gobnilp -g=settings_bn_learn.txt -f=dat data/{}'.format(sampleFileName))

'''load the adjacent matrix'''
adjmat = np.loadtxt("bn.mat")
