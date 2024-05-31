# 챗봇에서 사용하는 사전 파일 구축
import sys
sys.path.append("/Users/yeryeongseo/Documents/repositories/pythonStudy/charbotengine")
from utils.PreProcess import PreProcess
from tensorflow.keras import preprocessing
# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename.'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] # 헤더 제거
    return data

# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data(r'/Users/yeryeongseo/Documents/repositories/pythonStudy/charbotengine/train_tools/dict/create_dic.py')

for c in corpus_data:
    