#함수 데코레이터

def inner():
    print("계산처리 함수")
    
def outer(func):
    def wrapper():
        print("=" * 30)
        func()
        print("=" * 30)
    return wrapper

@outer
def inner():
    print("계산처리 함수")