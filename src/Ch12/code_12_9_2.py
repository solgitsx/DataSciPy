# 12.9 데이터를 설명하는 인덱스와 컬럼스 객체
## countries.csv 파일을 읽기

import pandas as pd 

df_my_index = pd.read_csv('d:/data/countries.csv', index_col = 0)
print(df_my_index[ ['area', 'population'] ])
