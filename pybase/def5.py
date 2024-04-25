#키워드 매개변수
def kwargs(**args):
    print(args)
    
kwargs(num = 10)
kwargs(name = "홍길동", age = 25)

#매개변수의 초기값 미리 설정
def myself(name, age, man = True):
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d세 입니다. " %age)
    if man : 
        print("남성입니다.")
    else:
        print("여성입니다.")
myself("홍길동", 30)