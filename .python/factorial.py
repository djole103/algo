import math
def factorial(num):
	if num == 0: return "0! = 1"
	output = "%i! = 1" % num
	for factor in range(2,num+1):
		output+=" x %i" % factor
	output += " = %i" % math.factorial(num)
	return output

test = 10
print(factorial(test))
