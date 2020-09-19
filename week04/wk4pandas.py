# 作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。

# 因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

# 作业要求：请将以下的 SQL 语句翻译成 pandas 语句：

# 读取 Excel 文件
# 在大多数基本的使用案例中，read_excel会读取Excel文件通过一个路径，并且sheet_name会表明需要解析哪一张表格。

import pandas as pd

# Returns a DataFrame
# D:\Program Files\Python37\Scripts>pip.exe install xlrd
# Use pip or conda to install fsspec.

# data = pd.read_excel('G://Python003-003//week04//data.xls', sheet_name='Sheet1')
import os
pwd = os.getcwd()
# print(pwd)# G:\Python003-003\week04
fname = os.path.join(pwd,'data.xls')
# print(fname)
# G:\Python003-003\week04\data.xls
data = pd.read_excel(fname, sheet_name='Sheet1')
# print(data)

'''
    id  age
0    1   11
1    2   22
2    3   33
3    4   44
4    5   55
5    6   66
6    7   77
7    8   88
8    9   99
9   10  110
10  11  121
11  12  132
12  13  143
13  14  154
14  15  165
'''

# 1. SELECT * FROM data;
print(data)

# 2. SELECT * FROM data LIMIT 10;
print(f'\n2.\n前10 行数据：\n{data.head(10)}')

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
# print(f"\n3\tid列：\t{data['id']}")

# 筛选标题为"还行"这一列
# df['还行']

# 4. SELECT COUNT(id) FROM data;
# 计数
# print(f"\n4.\tid列的数目：\t{len(data['id'])}")
# print(f"\n4.\tid列的数目：\t{data['id'].count()}")

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
# data = data.head(1000)
# print(data[data['age']>30])
# print(type(data))
# print(data.dtypes,data.info())
print(f"\n5.\n{data[(data['id'] < 1000) & (data['age'] > 30)]}")

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# print(f"6.\t{data.groupby(['id','order_id'])['order_id'].nunique()}")

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
# pd.merge(table1, table2, how='inner', left_on='id', right_on='id')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
# pd.concat([table1, table2])
# pd.concat([table1,table2]).drop_duplicates()

# 9. DELETE FROM table1 WHERE id=10;
# table1 = data[data['id']!=10].copy()
# print(f"\n9.table1:\n{table1}")
# print(f"\n9.\t{data.drop(data[data.id==10].index)}")
table1 = data.drop(data[data.id==10].index)
print(f"\n9.table1:\n{table1}")

# 10. ALTER TABLE table1 DROP COLUMN column_name;
# table1.__delitem__('age')
# print(f"\n10.table1删除了 age 列： \n{table1}")
print(f"\n10.\t{table1.drop(['age'],axis=1)}")