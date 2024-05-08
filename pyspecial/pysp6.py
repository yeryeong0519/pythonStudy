#일급 시민 활용 함수
def calc(op, a, b):
    op(a, b)
    
def add(a, b):
    print("두 수의 합 =", a + b)
    
def multi(a, b):
    print("두 수의 곱 =", a * b)
    
calc(add, 1, 2)
calc(multi, 3, 4)