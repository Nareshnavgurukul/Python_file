def binary():
	num = int(input("enter"))#13
	list = []
	list.append(num)
	while True:
		if num == 1:
			break
		else:
			num = num//2
			list.append(num)
	list.sort()
	base2 = ""#1101
	for i in list:
		if i%2==0:
			base2+="0"
		else:
			base2+="1"
	return(base2)
print(binary())

