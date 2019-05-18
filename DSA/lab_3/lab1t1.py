import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

df=pd.read_csv("F:/8sem/DSA/lab_3/wheat.csv")

my_dataframe = df[['area','perimeter']]
my_dataframe.plot.hist(alpha=0.75)
plt.title("16CS-78")
plt.show()

my_dataframe=df[['groove','asymmetry']]
my_dataframe.plot.hist(alpha=0.75)
plt.title("16CS-78")
plt.show()

