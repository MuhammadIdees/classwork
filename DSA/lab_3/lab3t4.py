# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:35:05 2019

@author: Phero-PC
"""

import pandas as pd
from pandas.tool.plotting import parallel_coordinates
import matplotlib
import matplotlib.pyplot as plt
	
matplotlib.style.use('ggplot') 
df = pd.read_csv("E:/Semester 8/DSA/files/wheat.csv") 
df1=df.drop(['area','perimeter'],axis=1)
plt.figure()
plt.title("16CS34")
parallel_coordinates(df1, 'wheat_type',alpha=0.4)
plt.show()