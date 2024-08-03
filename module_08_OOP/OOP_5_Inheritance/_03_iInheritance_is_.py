class SampleClass:
    def __init__(self, val):
        self.val = val


obj_1 = SampleClass(0)
obj_2 = SampleClass(2)
obj_3 = obj_1
obj_3.val = 3

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_3 is obj_1)

print(obj_1.val, obj_2.val, obj_3.val)

str1 = "У Мерри был "
str2 = "У Мерри был барашек"
str1 += "барашек"

print(str1 == str2, str1 is str2)

