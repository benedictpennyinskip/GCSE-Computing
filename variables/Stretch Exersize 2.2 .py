#Ben Penny-Inskip
#15-09-2014
#Stretch Exersise 2.3

import math

radius = float(input("what is the radius of your pool?"))
depth = float(input("what is the depth of your pool?"))

 
area = math.pi * radius**2
indisde_area = depth * area
indisde_area = round(indisde_area,2)

    
print("The area is:{0}".format(indisde_area))

