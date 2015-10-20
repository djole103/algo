rslt = []
check = {}

def realWord(string):
	return True

def allstr(string,chars): 
	for i in range(len(chars)):
		string+=chars[i]
		if realWord(string):
			rslt.append(string)
		allstr(string,chars[:i]+chars[i+1:])
		string = string[0:-1]
		
		

chars = ['a','b']
allstr("",chars)
print(rslt)

a = "abcde"
print(a[:2]+a[3:])
