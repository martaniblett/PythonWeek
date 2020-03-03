
file = open("teams.txt", "a+")
file.write ("This is a new line")
newfile=[]
for i in range (6):
    if i == 6:
        continue 
    newfile.append(file.readline())

file.close()

file = open("teams.txt", "a+")
