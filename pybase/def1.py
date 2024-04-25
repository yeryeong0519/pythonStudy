def add(a, b):
    return a + b
c = 12
d = 50
f = add(c, d)
print(f)
k = add(45, 70)
print(k)

def sumcalc(n):
    sum = 0
    for num in range(1, n + 1):
        sum += num
    return sum
print("합 = ", sumcalc(3))

def hello():
    return "안녕하세요"
print(hello())

