__author__ = 'Ben'
import random

class Deck(object):
    cards = []
    cardsremaining = 0
    def __init__(self, decks):
        self.shuffle(decks)

    def shuffle(self, decks):
        for n in range(1,14):
            self.cards.append(n)
            self.cards.append(n)
            self.cards.append(n)
            self.cards.append(n)
            self.cardsremaining += 4
        self.cardscards = random.shuffle(self.cards)

    def dealonecard(self):
        card = self.cards[0]
        self.cards = self.cards[1:]
        self.cardsremaining -= 1
        return card

    def printdeck(self):
        print(self.cards)
        print("Cards remaining: "+str(self.cardsremaining))

class Player(object):
    # players will have hands, which will be passed card/values
    # players will also have money, strategies, and the option to be player or computer controlled
    pass

def mainloop():
    deckshoe = Deck(1)
    deckshoe.printdeck()
    deckshoe.dealonecard()
    deckshoe.printdeck()

mainloop()
