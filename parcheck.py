def parCheck(s):
	stack = []
	good = False
	while(s):
		if s[0] == '(':
			stack.append(s[0])
			s = s[1:]
			continue
		if s[0] == ')':
			if not stack: break
			if stack[-1] == '(':
				stack.pop()
				s = s[1:]
			else:
				break
	if not stack and not s:
		good = True
	return good

#def fixit(s):
#	while(not parCheck(s)):
		


test = "(())()()(())"
print(parCheck(test))
