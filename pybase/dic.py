dic = {'name':'홍길동','phone':'010-2222-7777','address':'서울시 강남구'}
dic['birth'] = '19920520'
print((dic)['name'])
print((dic)['phone'])
score = {'홍길동':[78, 56, 90], '김철수' : [90, 85, 70]}
score['이영희']=[77, 95, 90]
del (score['김철수'])
score['홍길동'] = [80, 50, 90]
print(score.keys())
