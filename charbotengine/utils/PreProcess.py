# 전처리 과정 , 이걸 테스트하는게 test폴더에  preprocess_test.py
from konlpy.tag import Komoran
import pickle
import jpype

class PreProcess:
    def __init__(self, word2index_dic='', userdic=None): #생성자
        #단어 인덱스 사전 불러오기
        if(word2index_dic != ''):
            f = open(word2index_dic, "rb")
            self.word_index = pickle.load(f)
            f.close()
        
        #형태소 분석기 초기화
        self.komoran=Komoran(userdic=userdic)
        #제외할 품사 (어미, 접미사, 기호,...)
        self.exclusion_tags=[
            'JKS','JKC','JKG','JKO','JKB','JKV','JKQ','JX','JC','SF','SP','SS','SE','SO','EF','EC','ENT','ETM','XSN','XSV','XSA'
        ]
    #형태소 분석기 POS 태거 (pos는 튜플로 명사 동사 분류 아바지가 방에 드가신다)
    def pos(self, sentence):
        return self.komoran.pos(sentence)
    #불용어 제거 후 필요한 품사 정보만 가져오기 
    def get_keywords(self, pos, without_tag=False):
        f=lambda x: x in self.exclusion_tags
        word_list=[]
        for p in pos:
            if f(p[1]) is False: 
                word_list.append(p if without_tag is False else p[0])
        return word_list   
    # 키워드를 단어 인덱스 시퀀스로 변환
    def get_wordidx_sequence(self, keywords):
        if self.word_index is None:
            return []
        w2i = []
        for word in keywords:
            try:
                w2i.append(self.word_index[word])
            except keyError:
                    #해당 단어가 사전에 없는 경우 oov 처리
                    w2i.append(self.word_index['OOV'])
        return w2i
    
    #형태소 분서기를 komoran을 사용 userdic는 사용자 정의 파일을 바등ㅁ
    #  self.exclusion_tags는  적어놓은 품사들을 제거,즉 핵심키워드빼고 제거하겠따
    # pos는 문장에 대한 리스트로 품사로 분리
    # lambda 함수를 사용  f에 다 집어넣고  단어리스트에 false가 들어가면 for문 시행 품사와 단어 출력 true 단어만 출력  