import math

def count_ones(binary):
	ones = 0
	while(binary):
		ones+=1
		binary= binary & (binary-1)
	return ones

def palindrome(num):
#	digits = math.ceil(math.log(num,10))
#	print("Digits: ", digits)
#	if digits == 1: return True
	reverse = ""
	original = num
	while(num):
		reverse += str(num%10)
		num = math.floor(num/10)
	if int(reverse) == original: return True
	else: return False

def count_bits(num):
	bits = math.ceil(math.log(num,2))
