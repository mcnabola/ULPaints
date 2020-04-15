#!/usr/bin/env python3
import tkinter
import numpy as np
import matplotlib.pyplot as plt

# list_data will be a collection of data that will be transferred into a data type readable by / numpy plots / matplotlib
def graphing(): #list_data, ideal
    ## conversion needs to happen somewhere here

    values, = plt.plot([2.2, 2.3, 2.022, 1.97 ,2 ,2.1, 1.977], label = 'Sensor Values')
    staticVal, = plt.plot([2,2,2,2,2,2,2], label = 'Expected Values')

    plt.ylabel('Light Intensity')
    plt.xlabel('Period') ## plot against time array
    plt.legend(handles=[values,staticVal])
    plt.grid(True) # show grid
    plt.show()

graphing()
