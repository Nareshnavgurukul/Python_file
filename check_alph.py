list2="abcdefghijklmnopqrstuvwxyz"
list2=list(list2)

user=raw_input("enter the name/str")
stri=user.lower()
sum=0
for i in list2:
	sum=sum+1
	if i==stri:
		break
print "The postion of ",stri,"is ",sum,"."
