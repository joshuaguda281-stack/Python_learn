import colorsys
from dataclasses import dataclass
from sys import dont_write_bytecode
from urllib.response import addinfo

from my_functions import volume_cylinder, area_circle


def add(x, y,z):
    return x + y +z

# res = add(2,3,4) # args
# print(res)

def addition(z,*nums):
    total = 0
    for num in nums:
        total += num
    total = sum(nums)
    return total
# key and word arguments **kwargs
def save(**data):
    with open('data.txt','w') as file:
       for key, value in data.items():
           file.write(f"{key}:{value}\n")
                      
save(dob='2025-01-18', gender='male', color='black', name='Donald')


# print(addition(1,2,3,4,5,6,7,8,9))
# print(addition(100,70))

data = {"name":"Ken", "gender":"Male"}


def some_function(name, *scores, **details):
    pass

def cylinder(r,h):
    """
    calculates the volume of a cylinder and surface area
    parameters:
     radius and height of cylinder
    :returns volume and surface area
    """
    v= 22/7 * r * h
    sa = 22/7 * r **2 *2 + 22/7* r * 2 * h
    return v, sa

surf_area, volume = cylinder(r=20, h=10)
print(surf_area, volume)

sum([1,2,3])



#lambda functions
divider = lambda x, y : x//y

area_circle = lambda r : 22/7 * r * r

print(divider(45, 7))

res = area_circle(5)
print(res)

# save(dob='2025-01-18', gender='male', color='black', name='Donald')