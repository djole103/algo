def combstr(string,cur=""):
	strings = []
	for i in range(len(string)):
		strings.append(cur+string[i])
		strings += combstr(string[:i] + string[i+1:],cur+string[i])
	return strings
#doesn't work duplicates initial permutation
def permstr(string):
	perms = []
	for i in range(len(string)):
		for n in range(i,len(string)):
			perms.append(string[:i] + string[i+1:n+1] + string[i] + string[n+1:])
	return perms

test = "abc"
print(permstr(test))

	
