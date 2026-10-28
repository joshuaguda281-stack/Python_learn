# functions
from yt_dlp.extractor import oftv


def greet():
    print("Hello, welcome to python")

# use == call
greet()
greet()
greet()

def greet(user):
    print(f"Hello {user}, welcome to python")

# greet("Joshua")
# greet("ruth")
# greet("Rafael")

def area_circle(radius, precision =3):
    a = 22/7 * radius * radius
    result = round(a, precision)
    print(result)


area_circle(radius:2.9, precision:2)
area_circle(radius:6.9, precision:0)