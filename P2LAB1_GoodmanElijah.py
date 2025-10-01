# Elijah Goodman
# 09/24/25
#P2LAB1 
#Create a program that gives the radius, the diameter, the circumference, and the area of a circle.
import math

radius = float(input("Enter the radius: "))

cir = 2 * math.pi * radius
diam = 2 * radius 
area = math.pi * (radius ** 2)

print(f"The diameter of the cirlce is {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")