import time
start = time.time()
sum = 0
for num in range(1001):
    sum+=num
end = time.time()
print("1부터 1000까지 더하는데 걸린 시간 =", (end-start))