list=["naresh","HP","Asus","Asus","naresh","naresh","naresh","pawan","HP","naresh","pawan","HP","naresh","HP","Asus","naresh","HP","Asus"]
new=[]
pair=0
for i in list:
	if i in new:
		continue
	else:
		new.append(i)

		for A in list:
			if A==i:
				print i,
				pair=pair+1 
		pair=pair/2
		print ": the pair of",i,pair
		pair=0