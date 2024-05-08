#클로저 : 지역변수가 지속기간이 긴 함수에 의해 계속 사용된다면 해석기는 이 변수를 없애지않고 클로저
def makeHello(message):
    #내부함수(지역함수)
    def hello(name):
        print(message + ", " + name)
    return hello

enghello = makeHello("Good Morning")
hanhello = makeHello("안녕하세요")
