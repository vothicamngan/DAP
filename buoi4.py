import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')
# print(df.describe())
# # df_price = df.loc[:,'Price']
# # print(df_price)

# df_a = df.pivot_table(values='Price', index='ProductName', columns='Year', aggfunc='mean')
# print(df_a)
# df_b = df.pivot_table(values='Price',columns='Year',aggfunc='max')
# print(df_b)
# df_c = df.pivot_table(values='Price',index='ProductName',aggfunc='max')
# pf_d = df.pivot_table(values=['Price', 'Month'], index='ProductName', columns="Place", aggfunc={'Price':'sum', 'Month':'mean'})
df_f = df.pivot_table(values='Price', index='ProductName', columns='Year', aggfunc='mean')
pf_g = df.pivot_table(values=[ 'Year','Price'], index='ProductName',  aggfunc={'Year':'max','Price':'mean' })
print(pf_g)