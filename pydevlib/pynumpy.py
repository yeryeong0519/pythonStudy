import numpy as np

# 1.터미널에 pip install numpy 설치

#챗봇 엔진 개발에 필요한 딥러닝모델을 설계할 때 데이터 분석이 중요하다. 
    # 1. 데이터분석=>다양한 수치 계산과 과학적인 접근법 
    # 2. numpy라이브러리=>백터 및 행렬 연산에 필요한 기능 제공




arr=np.array([1,2,3])
print(arr)
print(type(arr))
matrix=np.array([[1,2,3],[4,5,6]]) #numpy 2X3행렬 생성
print(matrix)
a=np.array([[1,2],[3,4]])
b=np.array([[1,1],[1,1]])
c=a+b
print(c)