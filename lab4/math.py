import math
#1
degree=int(input("Input degree:"))
print("Output radian:"+str(math.radians(degree)))

#2
height=int(input("Height:"))
f_value=int(input("Base,first value:"))
s_value=int(input("Base,second value:"))
print(height*(f_value+s_value)/2)

#3
num_sides=int(input("Input number of sides:"))
lenght_sides=int(input("Input the length of a side:"))
a=360/(num_sides)
triangle_area=(lenght_sides**2)//(4*math.tan(math.radians(a/2)))
print("The area of the polygon is:"+str(num_sides*triangle_area))

#4
lenght=float(input("Length of base:"))
height=float(input("Height of parallelogram:"))
print(lenght*height)


