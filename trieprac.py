create_trie(*words):
	root = {}
	for word in words:
		curDict = root
		for let in word:
			curDict = curDict.setdefault(let,{})
		curDict["_end"] = "_end"
	return root
