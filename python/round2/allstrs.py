def allstrs(str, s = ''):
	if str == '': 
		return s
	results = []
	for i in range(len(str)):
		print("i:%i , str:%s , s:%s " % (i, str, s))
		s += str[i]
		results.append(allstrs(str[:i] + str[i+1:], s))
		s = s[:-1]
	return results

TEST = 'abc'

print(allstrs(TEST)) 
