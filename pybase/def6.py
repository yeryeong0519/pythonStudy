def calcsum(begin, end, step):
    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum

print("총합=", calcsum(5, 30, 3))
print("총합=", calcsum(20, 150))