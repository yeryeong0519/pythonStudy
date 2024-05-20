import pandas as pd
data = {'age':[23, 43, 12, 45],
        'name':['철수', '길동', '영희', '찬호'],
        'height' : [175, 183.5, 165.3, 177.8]}
x = pd.DataFrame(data, columns = ['name', 'age', 'height'])
print(x)
print(x.name)
