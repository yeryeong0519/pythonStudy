import time
print(time.time())
print(time.ctime())
now = time.localtime()
print("%d년%d월%d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("현재 시간은 %d시 %d분 %d초입니다.")