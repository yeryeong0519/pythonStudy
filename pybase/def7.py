def calcsum(begin, end, step):
    sum =0 
    for num in range(begin, end+1, step):
        sum+=sum
    return sum
print("총합=", calcsum(1, 10, 2))
print("총합 = ", calcsum(begin = 1, end = 10, step = 2))
print("총합 =", calcsum(step = 2, end = 10, begin = 1))