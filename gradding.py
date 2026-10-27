score = int(input("Enter score: "))
# if statements
if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 50 <= score < 60:
    print("E")
elif 40 <= score < 50:
    print("F")
else:
    print("Fail Terribly")

if score >= 90:
    print("excellent")
else:
    print("repeat")
