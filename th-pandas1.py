import pandas as pd
df = pd.read_csv("FoodPrice_in_Turkey.csv")
df_price = df.loc[:,'Price']
print(df_price)