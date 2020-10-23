
#taking a string input
a_string = (str(input("Please enter your 12-digit ISBN with spaces: ")))

#mapping and splitting the string to integers
list_1 = a_string.split()
map_object = map(int, list_1)

list = list(map_object)

#print the full ISBN and check digit
print("Your ISBN is ", list[0],list[1],list[2],"-",list[3],"-",list[4],list[5],list[6],"-",list[7],list[8],list[9],list[10],list[11],"-?")

chk_digit = 10 - ((list[0] + (3 * list[1]) + list[2] + (3 * list[3]) + list[4] + (3 * list[5]) + list[6] + (3 * list[7]) + list[8] + (3 * list[9]) + list[10] + (3 * list[11])) % 10 )
print("The check digit is ", chk_digit)

