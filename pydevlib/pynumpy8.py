import numpy as np
zero_vector=np.zeros(3)
print(zero_vector) #1차원적 제로백터 생성

zero_matrix=np.zeros((4,3)) # 4x3 행렬  
print(zero_matrix)

my_array=np.zeros(15).reshape(3,5)
my_array+=4
print(my_array) #3행 x5열 행렬에 모두 4로 값이 초기화