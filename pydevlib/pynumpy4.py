import numpy as np
x=np.array([1,3,5]) #리스트를 numpy형식으로 변환한다음 x에다가 넣었다고 보면된다 (1차우너배열)
print(x.mean()) #평균을 구하는 메소드 mean 
print(x.shape) 
a=np.array([[1,2,3],[3,4,5]]) # 2차원배열
print(a.shape)
b=np.array([1,3,5,7,9,11]).reshape(3,2) #reshape 는 1차원 배열을 2차원 배열로 만들어준다
print(b)
c=np.ones([3,4]) #ones메서느는 2차원 배열을 1의 값으로 채워서 만들어줌
print(c)