def make_trie(*words):
	root = {}
	curr_dict = {}
	for word in words:
		curr_dict = root
		for letter in word:
			curr_dict = curr_dict.setdefault(letter,{})
		curr_dict['_end_'] = '_end_'
	return root 

yo = make_trie("dog","cat","bob","boob","dogger","scath","cats")
print(yo)
