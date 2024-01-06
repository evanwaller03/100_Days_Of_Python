student_heights = input().split()

totalheight = 0
num_students = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    totalheight += student_heights[n]
    num_students += 1

avg = totalheight//num_students

print(f"Total Height: {totalheight}\nNumber of Students: {num_students}\nAverage Height: {avg}")
    

