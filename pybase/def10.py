a = 5
def test(a):
    a += 10
    return a
a = test(a)
print(a)

rate = 0.9
#사용자 정의 함수
def sales():
    print("오늘의 할인율: ", rate)
#사용자 정의 함수
def sales2():
    price = 1000
    print("판매가격:",price*rate)