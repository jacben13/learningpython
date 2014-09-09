__author__ = 'Ben'
import random


class Deck(object):
    cards = None
    cards_remaining = None
    starting_decks = None

    def __init__(self, decks):
        assert type(decks) == int
        self.starting_decks = decks
        self.cards_remaining = 0
        self.cards = []
        self.shuffle()

    def shuffle(self):
        for d in range(self.starting_decks):
            for n in range(1, 14):
                self.cards.append(n)
                self.cards.append(n)
                self.cards.append(n)
                self.cards.append(n)
                self.cards_remaining += 4
        random.shuffle(self.cards)

    def deal_one_card(self):
        if self.cards_remaining <= 0:
            self.shuffle()
        dealt_card = self.cards.pop()
        self.cards_remaining -= 1
        if self.cards_remaining <= 0:
            self.shuffle()
        return dealt_card

    def print_deck(self):
        print(self.cards)
        print("Cards remaining: " + str(self.cards_remaining))


class Player(object):
    # players will have hands, which will be passed card/values
    # players will also have money, strategies, and

    money = 0
    hand = []
    card_values = {"acelow": 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10,
                   "acehigh": 11}
    card_names = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack',
                  12: 'Queen', 13: 'King'}

    def __init__(self, money):
        self.money = money
        self.hand = []

    def get_card(self, d):
        # assert d is isinstance(object, Deck)
        self.hand.append(d.deal_one_card())

    def clear_hand(self):
        self.hand = []

    def get_total(self):
        total = 0
        aces = 0
        for c in self.hand:
            if c == 1:
                aces += 1
            elif c > 10:
                c = self.card_values[c]
            total += c
        if total + (aces * 10) <= 21:
            total += aces * 10

        return total

    def dealer_showing(self):
        return self.hand[1:]

    def dealer_showing_total(self):
        total = 0
        aces = 0
        for c in self.hand:
            if c > 10:
                c = self.card_values[c]
            total += c
        total -= self.card_values[self.hand[0]]
        return total

    def bust_or_not(self):
        return self.get_total() > 21

    def return_status_string(self, player_number):
        s = ""
        if player_number == 0:
            s += "\nDealer has all the money"
            s += "\nShowing: "
            for c in self.hand[1:]:
                s += self.card_names[c] + " "
            s += "for a total of\n"
            s += str(self.dealer_showing_total()) + "\n"
        else:
            s += "\nPlayer " + str(player_number) + " has " + str(self.money) + " money"
            s += "\nContains: "
            for c in self.hand:
                s += self.card_names[c] + " "
            s += "for a total of\n"
            s += str(self.get_total()) + "\n"
        return s


def initialize_players(number, money):
    players = []
    # add extra player to act as the dealer
    #the dealer will be players[0]
    for x in range(number + 1):
        players.append(Player(money))
    return players


def initial_deal(players_list, deck):
    for p in players_list:
        p.get_card(deck)
    for p in players_list:
        p.get_card(deck)

def mainloop():
    shoe = Deck(1)
    players = initialize_players(2, 1000)

    initial_deal(players, shoe)

    for i, p in enumerate(players):
        print(p.return_status_string(i))


mainloop()
#TODO implement app loop logic
#TODO implement strategies
#TODO implement dealer strategy
#TODO implement winning/losing and money transactions