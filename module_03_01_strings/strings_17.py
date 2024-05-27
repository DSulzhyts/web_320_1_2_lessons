import re

reg_1 = re.compile('course.topic.part.a')
# string_1 = """course topic*part/a"""
# print(bool(reg_1.match(string_1)))
#
# reg_2 = re.compile('course\\d\\d')
# string_2 = "mycourse12part23"
# print(bool(reg_2.search(string_2)))
#
# reg_3 = re.compile('part\\D001')
# string_3 = "part/001"
# print(bool(reg_3.search(string_3)))
#
# reg_4 = re.compile('user\\s24')
# string_4 = "user\n24"
# print(bool(reg_4.search(string_4)))
#
# reg_5 = re.compile('Bond\\S007')
# string_5 = "Bond-007 agent"
# print(bool(reg_5.search(string_5)))
#
# reg_6 = re.compile('\\w\\w555')
# string_6 = "FD555"
# print(bool(reg_6.search(string_6)))
#
# reg_7 = re.compile("Python\\W")
# string_7 = "Python*"
# print(bool(reg_7.search(string_7)))
#
# reg_8 = re.compile("[0-5]+[A-Ca-c]")
# string_8 = "012345abc"
# print(bool(reg_8.search(string_8)))
#
# reg_9 = re.compile('\\([^B-Db-d]\\)')
# string_9 = "(b)"
# print(bool(reg_9.search(string_9)))

reg_10 = re.compile('student\\d{5}')
string_10 = "student12345"
print(bool(reg_10.search(string_10)))

reg_11 = re.compile('student\\d{3,5}')
string_11 = "student12345"
print(bool(reg_11.search(string_11)))

reg_12 = re.compile('student\\d{3,}')
string_12 = "student12312654464"
print(bool(reg_12.search(string_12)))

reg_13 = re.compile('student\\d{,2}')
string_13 = "student12"
print(bool(reg_13.search(string_13)))


reg_14 = re.compile('come?')
string_14 = "com."
print(bool(reg_14.search(string_14)))

reg_15 = re.compile('student\\d+')
string_15 = "student1"
print(bool(reg_15.search(string_15)))
