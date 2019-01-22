def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print "Kya main print ho payungi? :-("
    return food
    print "Lekin main toh pakka nahi print hounga :'("
food=menu("monday")
print food






n=input()
for i in range(1,n+1):
	for j in range(i):
		print i,
	print ""




n=input()
i=0
while(i<=n):	
	j=0
	while(j<=i):
		print(i),
		j+=1
	print""
	i+=1



n=input(),
i=1
while(i<=n):	
	print (str(i)+" ")*i
	i+=1


s=0
i=1
while i<=n:
	h=1
	while h<=i:
		s+=1
		print s,
		h+=1
	print ""
	i+=1

