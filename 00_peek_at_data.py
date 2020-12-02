#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:05:39 2020

@author: philippmetzger
"""

#%% Import libaries
import pandas as pd
import os

#%% Load data
data = pd.read_csv(os.path.join('Data', 'donors.csv'), sep=',', index_col=0)

#%% Testing debugging
for i in range(10):
    print('Vor breakpoint')
    print(i)
    print('Nach breakpoint')