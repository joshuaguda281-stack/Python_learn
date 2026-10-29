import math


class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("radius must be a non-negative number")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def print_details(self):
        print("radius", self.radius)
        print("area", self.area())
        print("perimeter", self.perimeter())

c1 = Circle(14)
c2 = Circle(15.98)

c1.print_details()
print(c1.area())
