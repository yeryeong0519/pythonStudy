from konlpy.tag import Komoran
komo = Komoran(userdic ='./user_dic.tsv')
text = "우리 팻봇은 엔엘피를 좋아해"
pos = komo.pos(text)
print(pos)

#컴퓨터는 자연어를 처리 할 수 없다. 컴퓨터는 기계어
