# take input of student details

name = input("Please enter your name: ")
score_1 = int(input("Please enter your homework score: "))
score_2 = int(input("Please enter your assessment score: "))
score_3 = int(input("Please enter your final exam score: "))

def hw_calculate(score):
    if score >= 20:
        return "Pass"
    else:
             return "Fail"

def as_calculate(score):
    if score >= 35:
        return "Pass"
    else:
            return "Fail"

def fe_calculate(score):
    if score >= 40:
        return "Pass"
    else:
             return "Fail"

def percent_calc(res_1, res_2, res_3):
    perc_result = ((res_1 + res_2 + res_3) / 175) * 100
    print(name, "Your percentage score was", perc_result)
    return perc_result

hw_calculate(score_1)
as_calculate(score_2)
fe_calculate(score_3)
perc_result = percent_calc(score_1, score_2, score_3)

if perc_result >= 75:
    print("You got an A!")
elif perc_result >= 60:
    print("You got a B!")
elif perc_result >= 50:
    print("You got a C!")
else:
    print("You failed!")



