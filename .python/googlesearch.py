dictionary = {}
alphabet = []

def insert_checkp(inp):
	results = []
	for i in range len(inp):
		for letter in alphabet:
			close = inp[:i] + alphabet + inp[i:]
			if close in dictionary:
				results.append(close) 
	return results

def extra_check(inp):
	results = []
	for i in range len(inp):
		close = inp[:i] + inp[i+1:]
		if close in dictionary:
			results.append(close)
	return results

def swap_check(inp):
	results = []
	for i in range len(inp):
		for letter in alphabet:
			modded = inp
			modded[i] = letter
			if modded in dictionary:
				results.append(modded)
	return results

def didyoumean(inp):
	missing = insert_check(inp)
	extra = extra_check(inp)
	swapd = swap_check(inp)
	return missing + extra + swapd
