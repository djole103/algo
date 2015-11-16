def permutationsRec(elems):
	rslt = []
	for i in range(len(elems)):
		smaller = permutationsRec(elems[:i] + elems[i+1:])
		if smaller:
			for perm in smaller:
				rslt.append(perm[:i] + elems[i] + perm[i:])
	return rslt		


print(permutationsRec([1,2,3]))
