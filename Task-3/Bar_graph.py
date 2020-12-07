# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:33:04 2019

@author: hari1
"""
import matplotlib.pyplot as plt

def bar_chart(x,y,xLabel,yLabel,Title):
    plt.bar(x,y)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(Title)
    plt.legend(loc='upper right')

def Line_chart(x,y,xLabel,yLabel,Title):
    plt.xlabel("value")
    plt.ylabel("square of value")
    plt.plot(x,y)
    plt.title(Title)

def pie_chart(x,Label):    
    plt.axis("equal")
    plt.title("Selected stream")
    plt.pie(x,labels = Label, autopct="%1.1f%%")
