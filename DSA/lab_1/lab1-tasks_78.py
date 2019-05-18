# Question: 1
"""
•	Create a variable savings with the saving value 100.
•	Check out this variable by typing print(savings) in the script.

"""
savings = 100
#print (savings)

#Question: 2
"""
•	Create a variable factor, equal to 1.10.
•	Use savings and factor to calculate the amount of money you end up with after 7 years. Store the result in a new variable, result.
•	Print out the value of result.

"""

factor = 1.10
# Using formuling for calculating interest
result = savings * (1 + factor * 7)

#print (result)

#Question: 3
"""
•	Calculate the product of savings and factor. Store the result in year1.
•	What do you think the resulting type will be? Find out by printing out the type of year1.
•	Calculate the sum of desc(string) and desc and store the result in a new variable doubledesc.
•	Print out doubledesc. Did you expect this?
•	savings = 100, factor = 1.1, desc = "compound interest"

"""

year1 = savings * factor
#print ("Type of desc year1 = ", type(year1))

desc  = "Compound Interest"
doubledesc = desc + desc
#print("doubledesc = ", doubledesc)

#Question: 4
"""
•	Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
•	Print areas with the print() function.

"""

hall = 11.25
kit  = 18.00
liv  = 20.00
bed  = 10.75
bath =  9.50

area = [hall, kit, liv, bed, bath]
#print(area)

#Question: 5
"""
•	Finish the line of code that creates the areas list such that the list first contains the name of each room as a string, 
    and then its area. More specifically, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
•	Print areas again; is the printout more informative this time?

"""

area = [
    "Hall", hall,
    "Kitchen", kit,
    "Living Room", liv,
    "Bedroom", bed,
    "Bathroom", bath,
]

# print(area)

#Question : 6
"""
As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.
Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists. The script on the right can already give you an idea.
•	Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
•	Print out house; does this way of structuring your data make more sense?
•	Print out the type of house. Are you still dealing with a list?

"""
house = [
    ["Hall", hall],
    ["Kitchen", kit],
    ["Living Room", liv],
    ["Bedroom", bed],
    ["Bathroom", bath]
]

# print ("House : ", house)
# print ("Type of house : ", type(house))

#Question: 7
"""
•	Print out the second element from the areas list, so 11.25.
•	Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
•	Select the number representing the area of the living room and print it out.

"""

#print(house[0][0] + " : ", house[0][1])      # second element
#print(house[-1][0] + " : ",house[-1][1])     # last element
#print(house[2][0] + " : ",house[2][1])       # area of living room

#Question: 8
"""
•	Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, 
    that contains the sum of the area of the kitchen and the area of the bedroom.
•	Print this new variable eat_sleep_area.

"""

eat_sleep_area = house[-2][1] + house[-1][1]
#print("eat_sleep_area : ", eat_sleep_area)

#Question: 9
"""
•	Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
•	Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
•	Print both downstairs and upstairs using print()

"""

downstairs = area [0 : 6]
upstairs   = area [6 : ]

# print("Downstairs : ", downstairs)
# print("Upstairs : ", upstairs)

#Question: 10
"""
•	You did a miscalculation when determining the area of the bathroom; 
    it's 10.50 square meters instead of 9.50. Can you make the changes?
•	Make the areas list more trendy! Change "living room" to "chill zone".

"""

house [-1][1] = 10.5
house [2][0]  = "Chill Zone"

# print(house)

#Question: 11
"""
•	Use the + operator to paste the list ["poolhouse", 24.5]to the end of the areas list. Store the resulting list as areas_1.
•	Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.

"""

house1 = house + ["poolhouse", 24.5]
house2 = house1 + ["garage", 15.45]

#print("house2 = ", house2)

#Question: 12
"""
•	Use print() in combination with type() to print out the type of var1.
•	Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
•	Use int() to convert var2 to an integer. Store the output as out2.

"""

var1 = [1, 2, 3, 4]
var2 = True

#print("Type of var1 : ", type(var1))
#print("Length of var1: ", len(var1))

out2 = int(var2)
#print("out2 = ", out2)

#Question: 13
"""
•	Use + to merge the contents of first and second into a new list: full.
•	Call sorted() on full and specify the reverseargument to be True. Save the sorted list as full_sorted.
•	Finish off by printing out full_sorted.

"""

first  = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second
full_sorted = sorted(full, reverse = True)

#print("Full sorted: ", full_sorted)

#Question: 14
"""
•	Use the upper() method on room and store the result in room_up. Use the dot notation.
•	Print out room and room_up. Did both change?
•	Print out the number of o's on the variable room by calling count() on room and passing the letter "o" as an input to the method. We're talking about the variable room, not the word "room"!

"""

room    = "poolhouse"
room_up = room.upper()

#print("room = ",room)
#print("room_up = ",room_up)
#print("No of 'o's in room = ",room.count('o'))

#Question: 15
"""
•	Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
•	Call count() on areas to find out how many times 14.5 appears in the list. Again, simply print out this number.

"""

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

#print("Index of '20.0' : ", areas.index(20.0))
#print("Count of '14.5' : ", areas.count(14.5))

#Question: 16
"""
•	Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
•	Print out areas
•	Use the reverse() method to reverse the order of the elements in areas.
•	Print out areas once more.

"""

areas.append(24.5)
areas.append(15.45)
#print("areas : ", areas)

areas.reverse()
#print("reverse areas : ", areas)

#Question: 17
"""
•	Import the math package. Now you can access the constant pi with math.pi.
•	Calculate the circumference of the circle and store it in C.
•	Calculate the area of the circle and store it in A.

"""

import math

radius_of_circle        = 0.43
circumference_of_circle = 2 * math.pi * radius_of_circle
area_of_circle          = math.pi * pow(radius_of_circle, 2)

#print ("Circumferece of Circle : ", circumference_of_circle)
#print ("Area of Circle : ", area_of_circle)

#Question: 18
"""
•	Perform a selective import from the math package where you only import the radians function.
•	Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r∗ϕr∗ϕ, 
    where rr is the radius and ϕϕ is the angle in radians. To convert an angle in degrees to an angle in radians, 
    use the radians() function, which you just imported.
•	Print out dist.

"""
from math import radians

radius = 192500
angle  = radians(12)
distance   = radius * angle
#print("Distance : ", distance)

#Question: 19
"""
•	import the numpy package as np, so that you can refer to numpy with np.
•	Use np.array() to create a Numpy array from baseball. Name this array np_baseball.
•	Print out the type of np_baseball to check that you got it right.

"""

import numpy as np

baseball    = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
#print(type(np_baseball))

#Question: 20
"""
•	Create a Numpy array from height. Name this new array np_height.
•	Print np_height.
•	Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
•	Print out np_height_m and check if the output makes sense.

"""
height      = [62, 65, 69, 58, 67, 71]
np_height   = np.array(height)
#print("Height : ", height)

np_height_m = np_height * 0.0245
#print("Height in meters : ", np_height_m)

#Question: 21
"""
	Create a Numpy array from the weight list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting Numpy array as np_weight_kg.
	Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
    BMI=(weight(kg))/(height(m)^2 )
	Save the resulting numpy array as bmi.
	Print out bmi.

"""

weight         = [50, 70, 70, 82, 92, 65]
np_weight_kg   = np.array(weight) * 0.453592
bmi = np_weight_kg / pow(np_height_m, 2)

#print("BMI : ", bmi)

#Question: 22
"""
•	Create a boolean Numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
•	Print the array light.
•	Print out a Numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.

"""

#Question: 23
"""
•	Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
•	Print out the type of np_baseball.
•	Print out the shape attribute of np_baseball. Use np_baseball.shape.

"""
baseball = [
    [180 , 78.5, 1],
    [215 , 102.7, 1],
    [210 , 98.5, 1],
    [188 , 75.2, 1],
]
np_baseball = np.array(baseball)

#print("Type : "type(np_baseball))
#print("Shape of baseball : ", np_baseball.shape)

#Question: 24
"""
•	Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
•	Print out the shape attribute of np_baseball.

"""

#print("Shape of baseball : ", np_baseball.shape)

#Question: 25
"""
•	You managed to get hold on the changes in weight, height and age of all baseball players. It is available as a 2D Numpy array, update.
•	Add np_baseball and update and print out the result.

"""

update = [
    [170, 78.2, 20],
    [205, 112.7, 24],
    [212, 88.5, 23],
    [162, 74.2, 28],
]

np_update = np.array(update)

#print(np_baseball + np_update)

#Question: 26
"""
•	Create Numpy array np_height, that is equal to first column of np_baseball.
•	Print out the mean of np_height.
•	Print out the median of np_height

"""

np_height = np_baseball[:, 1]
#print("Mean = {}".format(np.mean(np_height)))
#print("Median = {}".format(np.median(np_height)))

#Question: 27
"""
•	The code to print out the mean height is already performed in previous question. Complete the code for the median height. Replace None with the correct code.
•	Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
•	Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct 

"""

np_weight = np_baseball[:,0]
np_height = np_baseball[:,1]

print("Mean = {}".format(np.mean(np_height)))
print("Median = {}".format(np.median(np_height)))
print("Standard Deviation = {}".format(np.std(np_weight)))
print("Correlation = {}".format(np.correlate(np_weight, np_height)))