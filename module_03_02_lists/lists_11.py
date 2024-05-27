student_marks = [
    ["Bob", 11, 8, 9, 10],
    ["Jane", 12, 9, 12, 11],
    ["Mark", 10, 11, 8, 9],
]

print(student_marks[0])
print(student_marks[1])
print(student_marks[2])

for student_mark in student_marks:
    print(student_mark)

print(student_marks[0][0])
print(student_marks[1][0])
print(student_marks[2][0])

# for i in range(len(student_marks)):
#     print()


student_marks = [
    {"Bob": [11, 8, 9, 10]},
    {"Jane": [12, 9, 12, 11]},
    {"Mark": [10, 11, 8, 9]},
]

print(student_marks[0]["Bob"][2])
print(student_marks[1]["Jane"])
print(student_marks[2]["Mark"])