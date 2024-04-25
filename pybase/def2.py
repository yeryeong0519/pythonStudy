# def add(a, b):
#     print("%d와 %d의 합은 %d입니다." %(a, b, a + b))
    
# add(7, 39)

def calcrange(begin, end):
    total = 0
    
    for num in range(begin, end + 1):
        if(num % 3 != 0):
            total += num
    return total
print("합 =", calcrange(20, 85))
#두 수의 차를 구하는 함수
def sub(a, b):
    return a-b
result = sub(b = 15, a = 30)
print("결과 = ", result)