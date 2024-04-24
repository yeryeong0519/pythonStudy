from copy import copy
a = [10, 20, 30]
b = a
c = copy(a)
print(a is b)
print(a is c)