import sys
sys.path.append(r"")
import pickle
from utils.PreProcess import PreProcess

f =open(r"")
word_index = pickle.load(f)
f.close()

sent = "내일 오전 10시에 탕수육 주문하고싶어"

p = PreProcess(useridc = r"")

pos = p.pos(sent)
keywords=p.get_keywords(pos, without_tag = True)
for word in keywords:
    try:
        print(word, word_index[word])
    except KeyError:
        print(word, word_index['OOV'])