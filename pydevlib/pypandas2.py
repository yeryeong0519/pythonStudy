import pandas as pd
temperatures = [[3.3, 34.5, 14.2, -10], [7.1, 32.1, 10.7, 2]]
seasons = ['봄', '여름', '가을', '겨울']
regions = ['서울', '부산']
data = pd.DataFrame(temperatures, index = regions, colums = seasons)
print(data)
print("="*50)
print(data.index)
print(data.columns)
print(data.values)
print(data['봄']['서울'])
