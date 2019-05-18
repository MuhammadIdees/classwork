#Question: 1
"""
•	print() the last item from both the year and the poplist to see what the predicted population for the year 2100 is.
•	Before you can start, you should import matplotlib.pyplotas plt. pyplot is a sub-package of matplotlib, hence the dot.
•	Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. 
    Don't forget to finish off with the show() function to actually display the plot.

"""

import matplotlib.pyplot as plt

year = [1994, 1995, 1998, 2000]
pop  = [2.59, 3.69, 5.33, 6.77]

# print('Year : {}\nPopulation: {}'.format(year[-1], pop[-1]))
# plt.plot(year, pop, label = 'Population')
# plt.xlabel('Year')
# plt.ylabel('Poputlation')
# plt.title('16CS-78')
# plt.show()


#Question: 2
"""
    Change the line plot to scattered plot

"""

# plt.scatter(year, pop)
# plt.xlabel('Year')
# plt.ylabel('Poputlation')
# plt.title('16CS-78')
# plt.show()

#Question: 3
"""
•	Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
•	Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
•	Don't forget to finish off with a plt.show() command, to actually display the plot.

"""

# import importlib
# importlib.reload(plt)
# import pandas as pd
# plt.clf()

# df = pd.read_csv('http://assets.datacamp.com/course/intermediate_python/gapminder.csv', index_col = 0)
# gdp_cap = list(df.gdp_cap)
# life_exp = list(df.life_exp)

# print('GDP Cap : {}\nLife Expectancy: {}'.format(gdp_cap[-1], life_exp[-1]))
# plt.plot(gdp_cap, life_exp)
# plt.xlabel('GDP Cap')
# plt.ylabel('Life Expectancy')
# plt.title('16CS-78')
# plt.show()

#Question: 4
"""
Create a histogram of list of prices

"""

prices = [100, 200, 300, 500, 500, 300, 700, 400, 900, 150, 
          600, 700, 300, 500, 650, 300, 200, 100, 500, 400]

# plt.hist(prices)
# plt.title('16CS-78')
# plt.show()

#Question: 5
"""
Create histogram of bin 5 and 20

"""
plt.hist(prices, bins = 5)
plt.title('16CS-78')
plt.show()

plt.hist(prices, bins = 20)
plt.title('16CS-78')
plt.show()
