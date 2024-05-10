import pandas

student_scores = {
    "student" : ["Evan", "Ian", "Meaghan", "Jerome", "Albert", "Karen", "Francesca", "David"],
    "score" : [51, 60, 89, 74, 12, 42, 64, 99]
}

student_dataframe = pandas.DataFrame(student_scores)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    if row.student == "Evan":
        print(row.score)

