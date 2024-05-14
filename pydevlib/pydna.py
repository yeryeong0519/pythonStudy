# f = open("/Users/yeryeongseo/Documents/repositories/pythonStudy/NM_207618.2.fna", "r")
# seq = f.read()
# print(seq)
with open("/Users/yeryeongseo/Documents/repositories/pythonStudy/NM_207618.2.fna", "r")as inf:
    data = inf.read().splitlines(True)  # 줄단위로 읽음
with open("/Users/yeryeongseo/Documents/repositories/pythonStudy/dna1.txt", "w")as outf:
    outf.writelines(data[1:])
f = open("/Users/yeryeongseo/Documents/repositories/pythonStudy/dna1.txt", "r")
seq = f.read()
seq = seq.replace("\n", "")
print(seq)