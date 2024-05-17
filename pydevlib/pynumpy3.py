import numpy as np

# 스칼라곱(크기만가지고)
# ※스칼라는 벡터 공간에서 벡터를 곱할 수 있는 양 (상수값)


a=np.array([[1,2],[3,4]])  #2x2행렬
k=10 #스칼라
c=k*a #스칼라곱
print(c)