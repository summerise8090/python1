# -*- coding: utf-8 -*-
"calculate kaoqin"
import sys
reload sys
sys.setdefaultcode('gbk')
import xlrd
import xlwt

filepath = r'C:\Users\admin\Documents\Tencent Files\568468543\FileRecv\201707研发考勤确认.xlsx'
exlobj = xlrd.open_workbook(filepath, 'r')
tbl = exlobj.sheets()[0]
cols = tbl.ncols
rows = tbl.nrows
print cols
print rows
print  tbl.row(2)[0].value
def GetRelaxPostion():
	for i in range(28,cols,1):
		strvale = tbl.row(1)[i].value
		strOT = '加班'
		if strvale.find(strOT):
			return i
	else:
		return -1

def GetIndex(str):
	for i in range(0, len(str)-1, 1):
		if str[i] == ':':
			return i
	else:
		return -1
def GetHourMin(strTime):
	idx = GetIndex(strTime)
	if idx == -1:
		return -1
	Hour = strTime[0:idx]
	Min = strTime[idx+1:]
	return Hour, Min

def IsWeekend(col):
	strvalue = tbl.row(1)[col].value
	print "value",strvalue
	if strvalue =='六'or strvalue == '日':
		return True
	else:
		return False

str = "08:10"
print GetIndex(str)
print GetHourMin(str)
print IsWeekend(12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
 	  
	
	
	
	
	