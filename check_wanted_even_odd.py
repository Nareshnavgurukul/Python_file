inn=input("enter the number: ")
iin=input("wanted")
odd=inn
total=0
while True:
	odd=odd-1
	inn+=1
	if inn%2==0:
		print inn,"even",
	if odd%2!=0:
		print odd,"odd"
		total+=1
	if total==iin:
		break
