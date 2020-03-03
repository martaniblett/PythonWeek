x1 = int(input("Please input FIRST digit "))
x2 = int(input("Please input SECOND digit "))
x3 = int(input("Please input THIRD digit "))
x4 = int(input("Please input FOURTH digit "))
x5 = int(input("Please input FIFTH digit "))
x6 = int(input("Please input SIXTH digit "))
x7 = int(input("Please input SEVENTH digit "))
x8 = int(input("Please input EIGHTH digit "))
x9 = int(input("Please input NINTH digit "))
x10 = int(input("Please input TENTH digit "))
x11 = int(input("Please input ELEVENTH digit "))
x12 = int(input("Please input TWELFTH digit "))

first_12_sum = (x1+3*x2+x3+3*x4+x5+3*x6+x7+3*x8+x9+3*x10+x11+3*x12)
#print (first_12_sum)
find_remainder = 10 - first_12_sum % 10
print (find_remainder)

x13 = first_12_sum % 10
print(x13)

