import sys
sys.path.append(r"D:\주간yw\pythonStudy\chatbotengine")
from utils.PreProcess import PreProcess
sent="내일 오전 10시에 탕수육 주문하고 싶어 맛있겟다.."

# 전처리 객체 생성
p=PreProcess(userdic=r'D:\주간yw\pythonStudy\chatbotengine\utils\user_dic.tsv')

#형태소 분석기 실행
pos=p.pos(sent)

#품사 태그와 같이 키워드 출력할테다
ret = p.get_keywords(pos,without_tag=False)
print(ret)

#품사 태그 없이 키워드 출력
ret =p.get_keywords(pos, without_tag=True)
print(ret)

