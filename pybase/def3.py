print("안녕하세요")
pass
print("잘가슈")
def calctotal():
    pass
print("가나다라")
score = 75
if score >= 90:
    pass
else:
    pass
#가변인수
def add_many(*nums):
    sum = 0
    for n in nums:
        sum+=n
    return sum
result = add_many(25, 36, 40)
print(result)
result1 = add_many(39, 59, 20, 49, 50, 38)
print(result1)