"format integer, for example:1000,after format,you will get 1,000"

def formatinteger(str):
	lsth = len(str)
	strb = ""
	if lsth<=3:
		
		print "the format is :%s"%str
		return True
		
	begin = lsth%3
	la=[]
	if begin !=0:
		la.append(str[0:begin]+',')
	for i in  range(begin,lsth-1, 3):
		if i+2 != lsth-1:
			la.append(str[i:i+3]+',')
		else:
			la.append(str[i:i+3])
	lhla = len(la)
	strb = ""
	for i in range(0,lhla,1):
		strb = strb+la[i]
	print "the format is :%s"%strb
	return True

while True:
	str = raw_input("pls input the integer you want to format,enter . to exit :");

	if str=='.':
		print"byebye"
		break
	formatinteger(str)
	