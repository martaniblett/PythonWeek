"""
file = (open("filename.txt", "r"))

outfile = ""

for line in range (10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline

file = open("filename.txt", "w")
file.write(outfile)
file.close()
"""
"""
file = open("teams.txt", "r")
lines = file.readline()
for lines in range(5):
    if lines == 0:
        lines = file.readline
print (lines)
for lines in range(5):
    if lines == 3:
        lines = file.readline
print (lines)
"""

with open("teams.txt", "r") as file:
    doc=file.readlines()
    print(doc[0])
    print(doc[3])





    

