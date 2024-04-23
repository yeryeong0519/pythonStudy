import time
def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min
result = gettime()
print("현재 시간은 %d시 %d분 %d초입니다." % (result[0], result[1], result[2]))
d, m = divmod(7, 3) #두 개의 값을 발생시킴
print("몫 = ", d)
print("나머지 = ", m)