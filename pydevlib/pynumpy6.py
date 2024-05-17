
import numpy as np


# list1=[1,2,3,4,5,6]
# print(list1[:3])

# list1=[[1,2],[3,4],[5,6]]
# print(list1[1][1])

# list1=[[1,2],[3,4],[5,6]]
# print(list1[:][1])

# list1=[[1,2],[3,4],[5,6]]
# print(list1[:,1])  #리스트는 2차원 접근 불가


# list1=[[1,2],[3,4],[5,6]]
# np_array=np.array(list1)
# print(list1[:,1])

# list1=[[1,2],[3,4],[5,6]]
# np_arr=np.array(list1)
# print(np_arr[:,1])
# print(np.array(list1[:,1]))

# 2리스트를 array메소드를 가지고 numpy배열로 변경
list1=np.array([[1,2],[3,4],[5,6]])
print(list1[:,1])

