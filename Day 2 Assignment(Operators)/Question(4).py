#Python program to find the area of a triangle whoes sides are given

import math
#accepts the three sides from the user
side1 = float(input("Enter first side:"))
side2 = float(input("Enter second side:"))
side3 = float(input("Enter third side:"))

#calculate the semi-perimeter
S= (side1+side2+side3)/2

#Calculate the area of triangle by using Heron's formula

area = math.sqrt(S*(S-side1)*(S-side2)*(S-side3))

#print the area of triagle
print(f"The area of triangle : {area:.2f}")
