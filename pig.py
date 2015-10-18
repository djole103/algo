class Pig:

	def __init__(self):
		self.p1score = 0
		self.p2score = 0
		self.options = ""
		self.onGoing = True
		self.winner = None
	def move(self):
		self.options()
		move = int(input())
		if move == 1:
			rolled = roll()
			#either gain nothing and return or re-move()
			conditions(rolled)
		elif move == 2:
			return hold()
	
	def checkWin(self):
		pass

	def startGame(self):
		while(onGoing):
			if turn = 0:
				self.p1score = move()
				checkWin()
			else:
				self.p2score = move()
		print("The winner is ___!!!")

	def options(self):
		print(self.options)
