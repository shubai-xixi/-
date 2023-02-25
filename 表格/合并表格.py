import os
import pandas as pd
import six
n = 0
l = []
for file in os.walk( '22级成绩/C班成绩' ):
	print(file)
	for table in file[2]: #file[2]是索引对应内容，好奇的话print一下对比就好
		path = file[0] + '/' + table
		data = pd.read_excel(path)
		n = n+1
		l.append(data)
		print('第'+str(n)+'个表已提取')

data_result = pd.concat(l)
data_result.to_excel ('试试啊.xlsx',index = 0 )