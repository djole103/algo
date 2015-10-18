from random import randint

class Pig:

	def __init__(self):
		self.turn = 1
		self.p1score = 0
		self.p2score = 0
		self.options = "1 : Roll the dice!\n2: Hold your score"
		self.onGoing = True
		self.winner = None
		print("WELCOME TO PIG!")

	def move(self):
		gains = 0
		while(1):
			print(self.options)
			print("Your current gainzzzzz: %i" % gains)
			move = int(input())
			if move == 1:
				rolled = self.roll()
				print("You rolled a %i!!!!!" % rolled)
				if rolled == 1: return 0
				else:  gains+=rolled
			elif move == 2:
				return gains
			else: print("Not a valid move punk!!")
	
	def roll(self):
		return randint(1,6)

	def checkWin(self):
		if self.p1score >= 100 or self.p2score >= 100:
			self.onGoing = False

	def startGame(self):
		while(self.onGoing):
			self.turn ^=1
			print("The score is\nPlayer 1: %i\nPlayer 2: %i" % (self.p1score,self.p2score))
			if self.turn == 0:
				print("Player 1's turn! Make a move buster")
				self.p1score += self.move()
			else:
				print("Player 2's turn! Go for gold")
				self.p2score += self.move()
			self.checkWin()
		print("The winner is !!!")

def main():
	while(1):
		newGame = Pig()
		newGame.startGame()

if __name__ == "__main__":
	main()
