'''
for a in range(1, 6):
    for b in range(a):
        print("*", end = "")
    print()
'''

for a in range(1, 10):
    for s in range(10-a):
        print("", end = "")
    for b in range(a*2-1):
        print("*", end = "")
    print()