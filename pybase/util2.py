def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += sum
        return sum
        