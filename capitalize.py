def capitalize(words):
	words = words.split()
	for i in range(len(words)):
		words[i] = words[i][0].upper() + words[i][1:]
	return words
print(capitalize("hey this should work"))
