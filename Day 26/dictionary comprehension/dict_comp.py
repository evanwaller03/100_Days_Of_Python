import random

names = ["Evan", "Ian", "Meaghan", "Jerome", "Albert", "Karen", "Francesca", "David"]

student_scores = {key:random.randint(0,100) for key in names}

print(student_scores)

passed_scores = {key:value for (key, value) in student_scores.items() if value >= 60}

print(passed_scores)