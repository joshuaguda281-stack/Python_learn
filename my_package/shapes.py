def circle(radius):
    """Calculate the area of a circle given its radius."""
    from math import pi
    return pi * radius ** 2

def rectangle(length, width):
    """Calculate the area of a rectangle given its length and width."""
    return length * width

def triangle(a, b, c, base, height):
    """Calculate the area of a triangle given its base and height."""
    s =(a + b + c) /  2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area**0.5

