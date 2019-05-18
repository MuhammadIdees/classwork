# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:25:49 2019

@author: Phero-PC
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
	
matplotlib.style.use('ggplot') 
df = pd.read_csv("E:/Semester 8/DSA/files/wheat.csv")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')	
ax.scatter(df.area, df.perimeter, df.asymmetry, c='r',marker='.')
plt.title('16CS34')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')
ax.scatter(df.width, df.groove, df.length, c='g',marker='.')
plt.title('16CS34')
plt.show()