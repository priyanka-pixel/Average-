student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)


total_heights = 0
for height in student_heights:
  total_heights += height
print(total_heights)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(number_of_students)

average_of_students = round(total_heights/number_of_students)
print(average_of_students)





