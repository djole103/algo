def allstr(chars,string = ""):
	results = []
	for i in range(len(chars)):
		string+=chars[i]
		#if validword(string): results.append(string)
		results.append(string)
		results += allstr(chars[:i] + chars[i+1:],string)
		string = string[:-1]
	return results
			
print(allstr(['a','b','c']))	
