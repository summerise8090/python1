"delete the first colum"
def thefirstindex(str, ch,index):
	lth = len(str)
	for i in range(0, lth-1, 1):
		if str[i] == ch:
			index = i 
			break
	else:
		index = -1
	return index

index = 0


fobj =open("d:\\a.txt","r")  
fw =  open("d:\\b.txt","w")  
allines = fobj.readlines()
for line in allines:
	lth = len(line)
	left = thefirstindex(line, '(', index)
	right = thefirstindex(line, ',', index)
	if left == -1 or right == -1:
		print "Error"
		break
	myline = line[0:left+1]+line[right+1: lth-1]+'\n'
	print myline
	#fw.writelines(myline)
fw.close()
fobj.close()


