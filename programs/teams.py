#write a new file called teams.txt

teamlist = ["Norwich", "Ipswich", "Fleetwood", "York", "Leeds"]

with open("teams.txt", "w") as file:
        for n in teamlist:
                file.write('%s\n' % n)              
 
file = open("teams.txt", "r")

print(file.readline())
file.readline()
file.readline()
print(file.readline())
file.close()
