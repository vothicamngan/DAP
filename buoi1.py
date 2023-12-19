import pandas as pd
import numpy as np

lst = [('Kế toán',2000), (' Công nghệ thông tin',25000), ('HR',5000)]
db = pd.DataFrame(lst, columns=['Nghề','Lương'])

lst2 = [('Tiên', 26),('Hải', 27), ('Hưng', 20),('Khanh',21),('Khánh', 22)]
db2  = pd.DataFrame(lst2, columns=['Tên', 'Tuổi'])

dic = {'Tên': ['Tiên','Hải','Hưng','Khanh','Khánh'],
       'Tuối': [26,27,20,21,22]}
db3 = pd.DataFrame(dic)

ser = {0:'Tiên', 1:'Hải', 2:'Hưng', 3:'Khanh',4:'Khánh',5:'Đạt'}
db4 = pd.Series(ser)

arr = np.array([26,27,20,21,22,23])
db5 = pd.Series(arr)

seri = pd.Series(10, index=[0,1,2,3,4,5])
db6 = pd.Series(seri)


dic1 = {'Name': ['Ngan','Đạt','Hưng'],
       'Age':[20,21,22],
       'Marks': [85.10,77.80,91.54]}
db7 = pd.DataFrame(dic1)
db8 =db7.set_index('Name')
print(db8)
print(db8.loc['Ngan'])