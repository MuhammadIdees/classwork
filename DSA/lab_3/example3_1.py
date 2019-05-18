import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

df = pd.read_csv ("F:/8sem/DSA/lab_3/wheat.csv", index_col = 0)
print(df.columns)

my_series = df.asymmetry

my_dataframe = df[['wheat_type', 'length', 'asymmetry']]

my_series.plot.hist(alpha=0.5)
plt.show()