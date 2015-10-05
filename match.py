def reg(A,B):
	if A>0 and B>0: return reg(A-1,B) + reg(A,B-1)
	elif A > 0: return 1
	else : return 1 

def winBy2(A,B):
	if A > 0 and B >0:
		if abs(A-B) == 1: return winBy2(max(A,B)-1,min(A,B))
		else: return winBy2(A-1,B) + winBy2(A,B-1) 
	else: return 1
		

def volleyball(A,B):
	if A<0 or B<0: return 0
	if (A > 25 and B<24) or (A<24 and B>25): return 0
	if A >= 24 and B >= 24: return reg(A,B) + winBy2(min(A,B)-24,max(A,B)-24)
	else: return reg(A,B)

def main():
	print(volleyball(A,B)


