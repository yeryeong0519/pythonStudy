import time
for dan in range(2, 10):
    print(dan, "단")
    for num in range(1, 10):
        print(dan, "X", num, "=", end = "=")
        time.sleep(0.2)
        print(dan * num)
    time.sleep(5)