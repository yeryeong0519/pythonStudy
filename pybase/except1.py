try:
    a = 10
    b = 2
    list = [10, 20, 30]
    print(list[2])
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱스 범위를 벗어났습니다.")
