def inttostr(num):
	convertString = "0123456789"
	digits = ""
	while(num):
		digit = num % 10
		digits = convertString[digit] + digits
		num = num//10
	return digits

def inttostrRec(num,base):
	convertString = "0123456789ABCDEF"
	if num < base: return convertString[num]
	return inttostrRec(num//base,base) + convertString[num % base]

test = 123
print(inttostrRec(test,16))
