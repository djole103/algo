phone = { '2' : 'ABC' ,
		  '3' : 'DEF' ,
		  '4' : 'GHI' ,
		  '5' : 'JKL' ,
		  '6' : 'MNO' ,
		  '7' : 'PQRS' ,
		  '8' : 'TUV' ,
		  '9' : 'WXYZ' }

results = []

def poss_text(dialed, sofar=""):
	global results
	if not dialed: 
		results.append(sofar)
		return
	for char in phone[dialed[0]]:
		poss_text(dialed[1:],sofar + char)

poss_text('234')
print(results)
