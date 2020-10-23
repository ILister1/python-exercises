names = str(input("Please enter five names: "))

x = names.split(", ")
namelist = list(x)
print(namelist)

for name in namelist:
    print(name, "is awesome!!")
