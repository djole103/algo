string = "dafdfhiddenmessageklvksldejfl"
if "hiddenmessage" in string: print("yup")
else: print("nup")

words = ["hey", "how", "are", "you"]
for index,word in enumerate(words):
    print(word,index)

#print("%s\n%s\n%s" % (repr(self.board[0],repr(self.board[1]),repr(self.board[2]))))

print("a"*5)

#if "x","x","x" == "x":
#	print("yup")
#else:
#	print("knew it")

test = "x" and "x"
print(test)
test2 = 'x' and 'o'
print(test2)

lst = [1,2,3]
print(iter(lst))

print(*lst)
lst2 = [11,22,33]
lst3 = zip(lst,lst2)
print(lst3)
print(*lst3)

lmb = lambda x : [x*2,x*3]
result = map(lmb,lst)
print(list(result))

print(list(zip(*([lst]*2))))
print([iter([1,2,3,4])]*2)

hmm = lambda a,k: zip(*([iter(a)]*k))
a = hmm([1,2,3,4,5,6],2)

print(list(a))

from itertools import islice
ten = [x for x in range(10)]
slicee = islice(ten,0,None,2)
print(list(slicee))
iten = iter(ten)
splitter = lambda a,k: islice(a,0,None,k)
for i in range (5):
	print(list(splitter(iten,2)))
print(list(islice(ten,0,None,5) for i in range(5)))
print(ten)
splitter2 = lambda a,k: zip(*(islice(a,i,None,k) for i in range(k)))
print(list(splitter2(ten,5)))

deep = [[1,2],[3,4],[5,6]]
flat = sum(deep, [])
print(flat)
deeper = [deep, deep]
#nope
#flatter = sum(sum(deep,[]),[])
#print(flatter)
flatter = [elem for l1 in deeper for l2 in l1 for elem in l2 ]
print(flatter)

l = [[]]*5
print(l)
l[1].append(1) 
print(l)
l[2].append(2)
print(l)
l[2][0] = 4
print(l)
print("")

l = list()
l.append(1)
print(l)
l.append(list())
print(l)
l[1].append(2)
print(l)
l.append(list())
l.append(list())
l[2].append(3)
print(l)
l[1].append(4)
print(l)

from itertools import cycle, islice
l = range(10)

print(10//2)

for i in range(1):
	print(i)
