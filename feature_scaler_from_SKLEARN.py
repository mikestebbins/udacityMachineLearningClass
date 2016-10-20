# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:56:28 2016

@author: mstebbins
"""

from sklearn.preprocessing import MinMaxScaler
import numpy
weights =  numpy.array([[115.],[140.],[175.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)

print rescaled_weight