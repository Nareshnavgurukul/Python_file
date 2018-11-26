# =========count how many time a number is repeating

count=0
number = input("enter number")
number=str(number)
for i in range(10):
	i = str(i)
	for p in number:
		if p == i:
			count+=1
	print i,"is",count,"times"
	count=0