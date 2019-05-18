# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:50:22 2019

@author: Phero-PC
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
	
matplotlib.style.use('ggplot') 

df = pd.read_csv("E:/Semester 8/DSA/files/wheat.csv")

df.plot.scatter(x='area', y='perimeter')
plt.title("16CS34")
plt.show()

df.plot.scatter(x='groove', y='asymmetry')
plt.title("16CS34")
plt.show()

df.plot.scatter(x='compactness', y='width')
plt.title("16CS34")
plt.show()
