temp = float(input ("Please enter temperature "))
if temp <= 20:
    print ("It is cold")
else:
    if temp >= 30:
        print ("It is hot")
    else:
        print("It is warm")


temp = float(input ("Please enter temperature "))
if temp <= 20:
    print ("It is cold")
elif temp < 30:
    print ("It is warm")
else:
    print ("It is hot")