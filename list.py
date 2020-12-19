a = ["physics","mathematics","chemistry","biology"]
print("set of values in list",a[2:3])
print("negative index ",a[-2])
a[2] = "english"
print("changed value of list a ",a)
del a[2]
print("value of list a after deletion",a)
a.insert(1,"social studies")
print("values after insertion",a)
a.reverse()
print("values after reversing ",a)
a.sort()
print("values after sorting ",a)
