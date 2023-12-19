import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('GDPlist.csv', encoding= 'unicode_escape')

print ("Thông tin của bảng là:")
print(df.info())
# 1. Bộ dữ liệu chứa bao nhiêu dòng, bao nhiêu cột
# TRẢ LỜI:Bộ dữ liệu có:
#   125 dòng
#   3 cột
# 2.Thang đo tương ứng của các thuộc tính được lưu trữ.
# Cột country có 125 dòng dữ liệu, không có dữ liệu null và được lưu dưới kiểu dữ liệu object
# Cột Continet có 125 dòng dữ liệu, không có dữ liệu null và được lưu dưới kiểu dữ liệu object
# Cột GDP (millions of US$) có 125 dòng dữ liệu, không có dữ liệu null và được lưu dưới kiểu dữ liệu int64

# plt.hist([df['Country'],df['GDP (millions of US$)']], bins=20)
# plt.title("Phân bố GDP")
# plt.xlabel("Quốc gia")
# plt.ylabel("Tổng GDP")
# plt.show()
# Từ biểu đồ, cho thấy được sự bộ bố GPD của các quốc gia không đồng điều

df_des = df.describe()
print(df_des)
# 1. Giá trị trung bình của GDP rồi vào khoảng 5.554$
# 2. Giá trị min là 1.06$ đang lệnh so với giá trị trung bình 1 khoảng khá xa


# grouped = df.groupby('Continent')
# num_country = grouped['Country'].count()
# print(num_country)
