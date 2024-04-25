#지역변수, 전역변수

a = 10
#사용자 함수 정의
def test(a):
    a += 5
    
test(20)
print(a)

def hello():
    temp = "안녕하세요"
    print(temp)
    
hello()
print(temp)