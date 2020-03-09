# open file teams.txt
file = open("teams.txt", "w")

# create variable to temporary store teams names
teams =["Man Utd", "Arsenal", "Man City", "Liverpool", "Everton"]

# loop through the file adding names to temp variable and skip names you want to drop
for i in range(5):
    file_team = teams[i] + "\n"
    file.write(file_team)
    
# close file
file.close()

#open file
file = open("teams.txt", "r")

# create empy string variable to store teams names to display
display_line = ""

# loop through file lines and store 1st and 3rd team
for line in range(5):
    if line == 1 or line == 3:
        display_line += file.readline()
    else:
        file.readline()

file.close()
print(display_line)
