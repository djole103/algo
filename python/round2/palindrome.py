def palindrome(num):
  digits = ''
  original = num
  while (num):
    digits+= str(num % 10)
    num = num // 10
  if int(digits) == original:
    print("yeaa")

palindrome(1001)
palindrome(111109)
