"""Calculate area of different
geometrical figures (circle,
rectangle, square, and triangle).
"""

import math

def area_of_circle(radius):
    return math.pi*radius*radius

def area_of_rect(length, width):
    return length*width

def area_of_square(side):
    return side*side

def area_of_triangle(base, height):
    return base*height/2


option = int(input("Whose area do you want to calculate?\n1 Circle\n2 Rectangle\n3 Square\n4 Triangle\n"))

if(option == 1):
    print(area_of_circle(int(input("Radius:"))))

elif(option == 2):
    print(area_of_rect(int(input("Length:")), int(input("Width:"))))

elif(option == 3):
    print(area_of_square(int(input("Side:"))))

elif(option == 4):
    print(area_of_triangle(int(input("Base:")), int(input("Height:"))))

else:
    print("Error: Input between 1-4")

