import math
#problem 1
r = 5
rsphere = 3
#radius of sphere is different from radius of circle
a = (math.pi*(r**2))
v = (4/3) * math.pi * rsphere**3
a_side = 3
b_side = 4
pyt = math.sqrt(a_side**2+b_side**2)
print(a, v, pyt)
#problem 2
first_name = "Glen"
last_name = "Frame"
concatenated_name = first_name + " " + last_name
concatenated_name_len = len(concatenated_name)
print(concatenated_name, concatenated_name.upper(), concatenated_name.lower(), concatenated_name_len)
#problem 3
age = 18
height = 6.3
weight = 201
inches = height * 12
print(type(age), type(height), type(weight))
BMI = ((weight/(inches**2))*703)
print(BMI)