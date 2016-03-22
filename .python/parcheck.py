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

def fixit(s):
	while(not parCheck(s)):
		count = 0
		idx = 0
		length = len(s)
		while(idx < length):
			if s[idx] == '(': 
				count+=1
				idx +=1
			elif s[idx] == ')':
				count-=1
				if count<0:
					s = s[:idx] + s[idx+1:]
					length = len(s)
				else:
					idx+=1
			else:
				idx+=1
		
		while count!= 0:
			idx = 0
			if	s[idx] == '(':
				count-=1
				s = s[:idx] + s[idx+1:]
				break
	return s	


test = "(()"
print(fixit(test))
