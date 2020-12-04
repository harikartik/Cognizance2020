# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:33:04 2019

@author: hari1
"""
import matplotlib.pyplot as plt


cities = ['Salem','Chennai','Coimbatore','Trichy','Banglore']
pop = [919150,8696010,2151466,1021717,2359748493]

plt.barh(cities,pop)
plt.xlabel('Population')
plt.ylabel('Cities')
plt.title("Population of cities")
plt.legend(loc='upper right')
