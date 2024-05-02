'''
def mul5(numlist):

result = mul5([2, 3, 5, 1])
print(result)
'''
# def mul5(num):
#     return num*5
# print(map(mul5,[2, 3, 5, 1]))

print(list(map(lambda num: num * 5, [2, 3, 5, 1])))