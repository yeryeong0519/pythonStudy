# class 클래스이름 : 
#     def ___init__(self):
#         생성자 내용
        
        
#     def 메소드이름(매개변수):
#         매소드 이용
        
class Account:
    def __init__(self, oname, balance):
        self.oname = oname
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        
    def withdraw(self, money):
        self.balance -= money
        
    def inquire(self):
        print("%s님의 잔액은 %d입니다." %(self.oname, self.balance))
        
shinhan = Account("김철수", 1000)   #신한 인스턴스 객체 생성
shinhan.deposit(5000)
shinhan.inquire()

nonghyup = Account("홍길동", 10000) #농협 인스턴스 객체 생성
nonghyup.withdraw(3000)
nonghyup.inquire()
        