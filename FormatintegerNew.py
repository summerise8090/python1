"format integer, for example:1000,after format,you will get 1,000"

def formatinteger(str):
	
	lsth = len(str)
	la=[]
	#throw up zeros
	for j in range(0, lsth-1,1):	
		if str[j] != '0':
			str = str[j:]
			break
	lsth = len(str)
	count = 0
	if lsth % 3 != 0 :
		count = 3 - lsth % 3
	
	for i in range(0, lsth, 1):
		if count == 3 :
			count = 0
			la.append(',')
		
		la.append(str[i])
		count = count + 1
		
	strb = ""
	lhla = len(la)
	for i in range(0, lhla, 1):
		strb = strb+la[i]
	print "the format is :%s"%strb
	
	return True
		


while True:
	str = raw_input("pls input the integer you want to format,enter . to exit :");

	if str=='.':
		print"byebye"
		break
	
	formatinteger(str)
	