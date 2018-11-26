# st=raw_input("input first ")
# other=raw_input("second ")
# total=""
# if len(st)==len(other): #if True then it will run
# 	for i in st:
# 		for k in other:  
# 			if i==k: 
# 				total+=i #if true then add to total
# 	if total==st:# if true 
# 		print "Alogram hai." 	
# else:
# 	print "Alogram nahi hai."



user=int(input())
index=1
h=1
while index<=user:
	while h<=index:
		print index,
		h=h+1

	print ""
	index=index+1


#