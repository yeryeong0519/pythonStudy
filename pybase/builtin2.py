eval("print('대한민국 + '파이팅')")
#리스트 중에서 양수만 걸러내기
def positive(numlist):
    result = []
    for num in numlist:
        if num > 0:
            result.append(num)
        return result
    
polist = positive([10, -5, 25, 0, -10, -30])
print(polist)