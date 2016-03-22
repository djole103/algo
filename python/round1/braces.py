matchingClose = { "(" : ")" ,
				  "[" : "]" ,
				  "{" : "}"}
checkOp = { ('(','[','{') : 'open',
				(')',']','}') : 'close' }
print(checkOp['('])

def openB(string, brace):
	for(i in range(string.len()): 
		if string[i] == matchingClose[brace]: break
		elif checkOp[string[i]] == 'open' : openB(string[i+1:-1],string[i])
		else: 
			testResults.append("NO")
			break

def braces(tstArray):
	testResults = []
	for test in tstArray:
		checkValid(test)	

def checkValid(string):
	if checkOC[string[0]] == 'open':
		openB(string[1:-1],string[0])
