#계산기 클래스
class Calculator : 
    def __init__(self, first, second):  #생성자
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result