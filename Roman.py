Roman = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
def RomanHelp(Dict):
	username = int(input("Enter you no. to convert into Roman:-"))
	if username in Roman:
		return(Roman[username])
	else:
		Sum = 0
		Str = ""
		for i in Roman:
			for R in Roman:
				if username!=0:	
					if R<username or username == R:
						username-=R
						Str+=Roman[R]
						break
		return(Str)
print(RomanHelp(Roman))
