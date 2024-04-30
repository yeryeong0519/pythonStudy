def calcsum(n):
    if(n <= 0) :
        raise ValueError
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum
try:
    print("sum of 1-100 is", calcsum(10))
except ValueError:
    print("입력값은 0이나 음수가 될 수 없다.")