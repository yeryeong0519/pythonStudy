a = [10, 20, 30]
print(id(a))
b = a
print(id(b))
a[1] = 69
print(a)
print(b)
c = a[:]