def tt():
	return (lambda x: x*i for i in range(5))

for t in tt():
	print(t(2))

#check lambda function differences between python 2 and 3
