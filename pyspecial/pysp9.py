#함수 데코레이터

def inner():
    print("지금은 파이썬의 고급문법")
    
def outer(func):
    print("=" * 20)
    func()
    print("=" * 20)
    
def hello():
    print("여러분 안녕하세요")

outer(inner)
outer(hello)