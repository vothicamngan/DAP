import pandas as pd
import matplotlib.pyplot as plt
# đọc dữ liệu, file dữ liệu thường có encoding = 'UTF-8' hoặc 'ISO-8859-1'
data=pd.read_csv('subset-covid-data.csv', encoding= 'UTF-8')
print("Top 5 dòng dữ liệu:")

print(data.head())
data.head()
print("Thông tin dữ liệu:")
print(data.info())
data.info()
print("Dữ liệu theo ngày:")
print(data.date.value_counts())
data.date.value_counts()
print("Lọc Dữ liệu nhiễu:")
print(data[data.date == '2020-04-12'])
cleaned_data = data[data.date == '2020-04-12']
print ("trung bình số ca mắc mới: " + str(cleaned_data.cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(cleaned_data.cases.median()))
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")

print("tổng số ca nhiễm và số ca ncủa các châu lục")
cleaned_data.groupby('continent')['cases','deaths'].sum()
print()