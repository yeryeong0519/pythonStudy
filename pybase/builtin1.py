print(abs(-5))
print(all([10, 20, 30]))    #반복 가능한 데이터 => 리스트, 튜플, 문자열, 딕셔너리
print(all([10, 20,  0]))    #요소중에 하나라도 거짓이 있으면 false
print(any([10, 20,  0]))    #요소중에 하나라도 참이 있으면 참
#all([])빈 값일때 True any([]) 빈 값일때 False
print(chr(97))
print(divmod(10, 3))
li = [10, 20, 30]
for num in li:
    print(num)