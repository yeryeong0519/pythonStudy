age = 25
print("당신의 나이는 {0} 세이군요".format(age))
name = "홍길동"
print("내 이름은 {0}입니다." .format(name))
print("내 이름은 {0}이고 나이는 {1}세입니다.".format(name, age))
print("오늘 날씨는 {weather}, 최고기온은 {temp}".format(weather = "맑고", temp = 23))
str = "대한민국"
print("{0:<10}파이팅".format(str))  # > 왼쪽정렬
print("{0:>10}파이팅".format(str))  # > 오른쪽정렬
print("{0:^10}파이팅".format(str))  # > 가운데정렬
print("{0:*<10}파이팅".format(str))  # > 왼쪽정렬
print("{0:*>10}파이팅".format(str))  # > 오른쪽정렬
print("{0:*^10}파이팅".format(str))  # > 가운데정렬
print("내 이름은 {0}이고 직업은 {{영업사원}}입니다.".format(name))  # > 가운데정렬
