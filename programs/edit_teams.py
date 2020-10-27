with open("teams.txt", "r+") as file:
    old = file.read() #stores the old file in full
    file.seek(0) #rewinds to the start of the file
    file.write("This is a new line\n" + old) #adds a new line, prints the whole file
