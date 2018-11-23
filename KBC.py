Q=["1.who is the owner of MS world?","2.45+52=........?","3.In which school I studyed?","4.founder of MS"]
opt1=["A)	Bill Gates","A)	197","A)	Amer Public","A) Akshay kumar"]
opt2=["B)	Steve jobs","B)	445","B)	Vidya and child","B)Lerry page"]
opt3=["C)	Tiger shroff","C)	97","C)	M.M school","C)	Bill Gates"]
key=["A","C","B","C"]
start=0
while start<len(Q):
	print Q[start]
	print opt1[start]
	print opt2[start]
	print opt3[start]
	print "                 "
	user=raw_input("Answer.........")
	print "                 "

	user=user.upper()
	if user==key[start]:
		print "Right answer :)"
	if user not in key:
		print "enter the valid option."
	else:
		print "Wrong answer:("
	start+=1
