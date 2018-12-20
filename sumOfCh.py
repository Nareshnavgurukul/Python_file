#this code will add only number from the given input
# it will also print number fron the given input

user=raw_input("enter ")
num=[]#I can alos take a list with 0 to 9 strtring number and it depend on range(10) loop
total=0
number=""
for i in range(10):
	i=str(i)
	num.append(i)
for char in user:	
	if char in num:
		number+=char
	else:
		number+=","

number=number.split(",")
for v in number:
	if v=="":
		continue
	else:
		print v
		total+=int(v)
print "\n"
print total ,"This is the total of all number"


