# Declaring variables for maths, chemistry and physics mark input
maths_mark = int(input("Please enter your maths mark: "))
chem_mark = int(input("Please enter your chemistry mark: "))
phys_mark = int(input("Please enter your physics mark: "))

# working out percentage score
perc_score = float(((maths_mark + chem_mark + phys_mark) / 300) * 100)
print("Your percentage score was ", perc_score, "%!")
# working out the grade based on the score

if perc_score >= 70:
    print("Your grade was A")
elif perc_score >= 60:
    print("Your grade was B")
elif perc_score >= 50:
    print("Your grade was C")
elif perc_score >= 40:
    print("Your grade was D")
else:
    print("You failed!")

