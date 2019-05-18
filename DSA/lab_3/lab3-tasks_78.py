import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

# #Question: 1
matplotlib.style.use('ggplot')

#load csv file and create a data frame
data = pd.read_csv ("F:/8sem/DSA/lab_3/wheat.csv")
my_dataframe = pd.DataFrame(data, columns = data.columns)

# slice including only the area and parameter feature
df_area_groove = my_dataframe.loc[:, ['area', 'groove']]
df_area_groove.plot.hist(alpha = 0.75)
plt.title('16CS-78')

# slice including only the grove and assymetry feature
df_area_perimeter = my_dataframe.loc[:, ['area','perimeter']]
df_area_perimeter.plot.hist(alpha = 0.75)
plt.title('16CS-78')

plt.show()


#Question: 2
my_dataframe.plot.scatter(x='area', y='perimeter')
plt.title("16CS-78")

my_dataframe.plot.scatter(x='groove', y='asymmetry')
plt.title("16CS-78")

my_dataframe.plot.scatter(x='compactness', y='width')
plt.title("16CS-78")

plt.show()

#Question: 3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')	
ax.scatter(my_dataframe.area, my_dataframe.perimeter, my_dataframe.asymmetry, c='r',marker='.')
plt.title("16CS-78")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')
ax.scatter(my_dataframe.width, my_dataframe.groove, my_dataframe.length, c='g',marker='.')
plt.title("16CS-78")
plt.show()

#Question: 4	 
df = my_dataframe.drop(['area','perimeter'],axis=1)
plt.figure()
plt.title("16CS-78")
pd.plotting.parallel_coordinates(df, 'wheat_type',alpha=0.4)

#Question: 5
plt.figure()
plt.title("16CS-78")
pd.plotting.andrews_curves(my_dataframe, 'wheat_type',alpha=0.4)

#Question: 6
img=mpimg.imread("F:/8sem/DSA/lab_3/image.jpg")
print(img.shape)
print(type(img))
plt.title('16CS-78')
plt.imshow(img)

plt.show()
