#키워드 매개변수
def kwargs(**args):
    begin = args['begin']
    end = args['end']
    sum = 0
    for num in range(begin, end + 1 ,step = 1):
        sum += num
    return sum

print("총합 = ", calcsum(begin = 1, end = 10, step = 2))
print("총합 =", calcsum(step = 2, end = 10, begin = 1))