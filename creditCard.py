user = input("enter you no.")#4215-2352-1220-2002
num = "0123456789-"
def three():
	for i in user:
		if i in num:
			ch = ""
			ch = i*3
			if ch in user:
				return("invalied")
	else:
		return("valied")

def credit():
	if user[0] == "4":
		if len(user)==19:
			if user[4] == "-" and user[9] == "-" and user[14] == "-":
				return(three())
		elif len(user)==16:
			return(three())
	else:
		return("invalied")
print(cradit())
