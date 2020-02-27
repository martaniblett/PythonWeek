biology_grade = float(input("Please input biology grade: "))
chemistry_grade = float(input("Please input chemistry grade: "))
physics_grade = float(input("Please input physics grade: "))

score = int((biology_grade+chemistry_grade+physics_grade)/3)
# print ("Average score", score)
if biology_grade < 40 or chemistry_grade < 40 or physics_grade < 40:
    print ("Fail")
else:
    if score < 40:
        print ("Fail")
    elif score < 50:
        print ("D")
    elif score < 60:
        print ("C")
    elif score < 70:
        print ("B")
    else:
        print ("A")
