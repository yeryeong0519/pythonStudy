score = 80
print("결과 =" + str(score))
print(sum([25, 36, 10]))
print(sum([41, 21, 15]))
tu = tuple("korea")
print(tu)
tu1 = tuple([10, 20, 30])
print(tu1)
name = ["홍길동", "김철수", "이영희"]
addr = ["서울시 종로구", "서울시 강남구", "서울시 영등포구"]
address = list(zip(name, addr))
print(address)
print(list(zip([10, 20, 30], [40, 50, 60])))
print(list(zip([10, 20, 30], [40, 50, 60], [70, 80, 90])))
print(list(zip("korea", "japan")))