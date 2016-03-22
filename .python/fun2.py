class Num:
	def __init__(self,num):
		self.val = num

	def changeDirect(self,new):
		self.val = new

	def changeNonD(self,new):
		intermediate = self.val
		intermediate = 5

	def changeNonD2(self,new):
		self.change(self.val,new)

	def change(self,val,new):
		val = new

def alter(num,new):
	num = new

n = Num(1)
print("The starting value: %i" % n.val)
n.changeDirect(2)
print("Changing it directly value: %i" % n.val)
n.changeNonD(3)
print("Set to variable and change that value: %i" % n.val)
n.changeNonD2(4)
print("Pass it directly into function value: %i" % n.val)


n2 = 1
alter(n2,2)
print(n2)
