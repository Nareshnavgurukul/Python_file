# =============counting a number how much time is repeting
a = input("enter the number")
a = str(a)
flag0 = 0
flag1 = 0
for i in a:
	if i == '0':
		flag0 = flag0 + 1
	if i == '1':
		flag1 = flag1 + 1	
print "0 : " ,flag0
print "1 : ",flag1	
