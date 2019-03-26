
N=[34,34,4,5,6,7,1,32,43,4434,76,655476235,985,444,-9999,55*67]
n = set(N)
n = list(n)
list(n)
k=[]
user=int(input("enter the wanted number "))
if user <=(len(n)):
	min=n[0]
	for f in range(user):
		for i in n:
			if min>i:
				min=i
		k.append(min)
		n.remove(min)
		min=n[0]
	print(k)
else:
	print("sorry str(user) element are not in this list")
