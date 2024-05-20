import pandas as pd
x = pd.Series(([7, 3, 5, 8]), index = ['서울', '대구', '부산', '광주'])
y = pd.Series([2, 4, 5, 1], index = ['대구', '부산', '서울', '대전'])
print(x)
print(x[['서울', '대구']])
print(x.index)
print(x.values)