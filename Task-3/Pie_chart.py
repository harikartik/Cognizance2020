# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 23:03:38 2019

@author: hari1
"""

import matplotlib.pyplot as plt
plt.axis("equal")

count = [3,5,5,10]
stream = ['Bio-CS','Bio-Math',"Math-CS","BS-CS"]
exp = [0.25,0,0,0]
plt.title("Selected stream")
plt.pie(count,labels = stream, autopct="%1.1f%%",explode = exp)
