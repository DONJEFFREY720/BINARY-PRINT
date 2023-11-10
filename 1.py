# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:18:49 2023

@author: Don Jeffrey
"""
from tkinter import*
root=Tk()
root.title("Title") 
root.geometry("500x500")
root.configure(bg="white")

import random
import matplotlib.pyplot as plt


data = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0]]


plt.imshow(data, cmap= 'gray')



