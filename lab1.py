import math
#problem 1
print((math.pi*(5**2)))
print(((math.pi*(3**3))*(4/3)))
print(math.sqrt(3**2+4**2))
#problem 2
full_name = "Glen Ferrara Frame"
print(len(full_name))
first_name = "Glen"
last_name = "Frame"
concatenated_name = first_name + " " + last_name
print(concatenated_name)
print(concatenated_name.upper())
print(concatenated_name.lower())
#problem 3
age = 18
height = 6.3
weight = 201
print(type(age))
print(type(height))
print(type(weight))
BMI = ((weight/((height*12)**2))*703)
print(BMI)