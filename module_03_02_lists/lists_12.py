student_marks = [
    ["Bob", 11, 8, 9, 10],
    ["Jane", 12, 9, 12, 11],
    ["Mark", 10, 11, 8, 9],
]

for i in range(len(student_marks)):
    for j in range(len(student_marks[i])):
        print(student_marks[i][j])

print()
for student_mark in student_marks:
    for student in student_mark:
        print(student)


print(student_marks.index(["Bob", 11, 8, 9, 10]))


student_marks = [
    ["Bob", 11, 8, 9, 10],
    ["Jane", 12, 9, 12, 11],
    ["Mark", 10, 11, 8, 9],
]

for student_mark in student_marks:
    if "Jane" in student_mark:
        print(student_mark.index(9))

