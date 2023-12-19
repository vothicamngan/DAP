import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')


# print(df.head())
# print(df.loc[:,'UmId'])
# print(df.loc[:,['Month','Year']])
# print(df.loc[4,'Month'])
# print(df.loc[df.Year >=2019])

# print(df.loc[0:10,'UmName':'Price'])
# df['Giảm giá'] = pd.Series('10%', index=df.index)
df.rename(columns={'Place':'Địa điểm','ProductName':'Tên SP'},inplace=True)
df['Giảm giá'] = '10%'
# df =df.append({'Địa điểm':'Na','ProductId':'RR','Tên SP':'Rice','UmId':10,'UnMane':'KG','Month':6,'Year':6,'Price':84.3785,'Giảm giá':'10%'}, ignone_index = True)
# df.drop('Giảm giá',axis=1, inplace=True)
df.drop(['Giảm giá','Year'],axis=1, inplace=True)
df.drop(1,axis=0,inplace=True)
df.replace(5,10 , inplace = True)
print(df.head())