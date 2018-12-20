st=raw_input("input first ")
other=raw_input("second ")
total=""
if len(st)==len(other): #if True then it will run
	for i in st:
		for k in other:  
			if i==k: 
				total+=i #if true then add to total
	if total==st:# if true 
		print "Alogram hai." 	
else:
	print "Alogram nahi hai."
