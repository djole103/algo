import random
deck = ['1C','1S','1H','1D','2C','2S'...]

class Player:
    def __init__(self):
        self.hand = []

    def takeCard(self,card):
        self.hand.append(card)

def dealCard(deck):
    randomIndex = randint(0,len(deck))
    card = deck[randomIndex]
    deck.pop(randomIndex)
    return card

def gameStart(numPlayers,cardsPerHand):
    global deck 
    player = dict()
    for i in range(1,numPlayers+1):
        player[i] = Player()
    
    for i in range(numPlayers*cardsPerHand):
        card = dealCard()
        player[(i%numPlayers) + 1].takeCard(card)

def main(numPlayers,cardsPerHand):
    while(1):
        wantToPlay = int(input("Do you want to play?\n1: Yes\n0: No\n"))
        if wantToPlay:
            gameStart(numPlayers,cardsPerHand)
        else: break

if __name__ == "__main__":
    main() 

