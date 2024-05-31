from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

def read_review_data(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        data = [line.split('\t') for line f.read().]
        data = data[1:]
    return data

start = time.time()

print('1)
review_data = read_review_data(r'')
        