dic = {'boy' : '소년', 'school':'학교','book':'책'}
dic['boy'] = '남자애'
dic['girl'] = '소녀'
dic2 = {'student' : '학생', 'teacher':'선생님','book':'서적'}
dic.update(dic2)
print(dic)
if 'school' in dic:
    print("사전에 있는 단어입니다.")
else:
    print("사전에 없는 단어입니다.")