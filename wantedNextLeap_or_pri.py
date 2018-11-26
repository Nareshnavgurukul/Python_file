user=input("enter the number to check leap year:- ")#it will take number to check leap year
wanted=input("enter the number how much you want. ")# how much you want to check input
Next=user #here I have assing the value of input(user)
Break=0 # break my loop if Break==wanted. 
phle="" #it will store all pri leap year one by one in the str(type)
agla="" #it will store all next leap year one by one in the str(type) 
while True: 
	Next+=1
	user-=1
	if ((user%4==0 and user%100==0) and user%400==0): #logic of leap
		if user>0:# this condition wiil always true if user>0 
			user=str(user) #all the time user value will str(user)
			phle+=user+","
			user=int(user)
	if ((Next%4==0 and Next%100==0) and Next%400==0): #logic of leap
		Next=str(Next)
		agla+=Next+","
		Next=int(Next)
		Break+=1 
	if Break==wanted:
		break

print phle,"phle leap year"
print agla,"Next leap year"
