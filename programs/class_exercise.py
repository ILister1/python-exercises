class students:
    def __init__(self, name, age, _class):
        self.name = name
        self.age = age
        self._class = "student"
    def test_score(self, res_1, res_2, res_3):
        total = res_1 + res_2 + res_3
        avg = total / 3
        return avg


name = input("Please input your name: ")
age = input("Please input your age: ")
score_1 = int(input("Please input score 1: "))
score_2 = int(input("Please input score 2: "))
score_3 = int(input("Please input score 3: "))

student_1 = students(name, age, "student")

print(student_1.name, "achieved an average score of ", student_1.test_score(score_1, score_2, score_3))






