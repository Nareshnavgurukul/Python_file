n=[34,4,5,6,7,1,32,43,4434,76,655476235,985,444,-9999,55*67]
k=[]
user=user("enter the wanted number ")
mx=n[0]
for f in range(user):
	for i in n:
		if mx<i:
			mx=i
	k.append(mx)
	n.remove(mx)
	mx=n[0]
print k


