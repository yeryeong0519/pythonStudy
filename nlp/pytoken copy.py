from konlpy.tag import Komoran

komo = Komoran()
text = "어머니가 방에 들어갑니다."

morphs = komo.morphs(text)
print(morphs)
pos = komo.pos(text)
print(pos)