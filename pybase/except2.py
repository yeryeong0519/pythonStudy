try:
    a = 10
    b = 2
    list = [10, 20, 30]
    print(list[2])
    result = a / b
    print(result)
except (ZeroDivisionError, IndexError):
    print("오류가 발생하였습니다.")

