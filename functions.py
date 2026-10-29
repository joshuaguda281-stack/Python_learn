# functions
import random

with open("students.txt", "a") as file:
    # file.write("77\n")
    # file.write("13\n")
    for temp in range(100):
      x = random.randint(-10, 65)
      file.write(str(temp)+"\n")

with open("students.txt", "r") as file:
    content = file.read() # zero parameters / 0 arguments
    print(content)