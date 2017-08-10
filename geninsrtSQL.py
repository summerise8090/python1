"read excel generate insert SQL"
# -*- coding: utf-8 -*- 

import  xdrlib ,sys
import xlrd

def isNum(str):
	lth = len(str)
	for i in range(0, lth-1,1):
		if str[i] not in '0123456789':
			return False
	else:
		return True
		
exlobj = xlrd.open_workbook(r'D:\teachers.xls', 'r')
fobj = file(r'E:\b.txt','w')

tbl = exlobj.sheets()[0]
rows= tbl.nrows
cols = tbl.ncols
strinsert = r'insert into TBLNAME VALUES ('
lines = ''
for i in range(0, rows, 1):
	for j in range(0, cols, 1):
		strvalue = tbl.row(i)[j].value
		if isNum(strvalue.encode('gbk')) != True:
			strvalue = "'"+tbl.row(i)[j].value+"'"
		if j == cols-1:
			lines =lines + strvalue + ');\n'			
		elif j == 0:
			lines = strinsert +strvalue+','
		else:			
			lines =lines+ strvalue+','
	
	print lines
	fobj.writelines(lines.encode('gbk'))
	
fobj.close()
