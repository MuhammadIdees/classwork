# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:08:36 2019

@author: Phero-PC
"""

import pandas as pd
from pandas.tools.plotting import andrews_curves
import matplotlib
import matplotlib.pyplot as plt
	
matplotlib.style.use('ggplot') 
df = pd.read_csv("E:/Semester 8/DSA/files/wheat.csv", index_col=0) 
print(df.columns)
plt.figure()
plt.title("16CS34")
andrews_curves(df, 'wheat_type',alpha=0.4)
plt.show()