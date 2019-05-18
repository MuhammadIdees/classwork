# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:55:44 2019

@author: Phero-PC
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread("E:/Semester 8/DSA/files/image.jpg")
print(img.shape)
print(type(img))
plt.title('16cs34')
plt.imshow(img)

