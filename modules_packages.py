#import my_functions
#
# print(my_functions.volume_cylinder(5, 3))

# import my_functions as walter
#
# walter.area_circle(radius=5, precision=4)

# from my_functions import area_circle, volume_cylinder
# print(volume_cylinder(5, 3))
# print(area_circle(radius=5, precision=4))

# from math import *
#
# print(sqrt(25))
# print(floor(5.7))
# print(round(5.7))
from my_package.shapes import circle, rectangle, triangle

print(circle(radius=5))
print(rectangle(length=5, width=3))
print(triangle(a=3, b=4, c=5, base=3, height=4))
