dic = {'name':'홍길동','phone':'010-2222-7777','address':'서울시 강남구'}
dkey = list(dic.keys())
dvalue = dic.values()
print(dkey)
print(dvalue)
print(dic.get('name'))
print(dic['phone'])
print(dic.get('phoe', "찾는 자료가 없습니다."))