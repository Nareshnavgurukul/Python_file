string="abcdefghijklmnopqrstuvwxyz"
user=raw_input("enter the name:-")
user=user.lower()
s=0
for i in string:
	for x in user:
		if x==i:
			s+=1
	if s>0:
		print i,"is",s,"time."
		s=0

