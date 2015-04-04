__author__ = 'Ben'
import random
import configparser

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

    def check_cards_remaining(self, number_of_players):
        if self.cards_remaining < number_of_players * 5:
            self.shuffle()

    def print_deck(self):
        print(self.cards)
        print("Cards remaining: " + str(self.cards_remaining))


class Player(object):
    # players will have hands, which will be passed card/values
    # players will also have money

    money = 0
    hand = []
    blackjack = False
    card_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10}
    card_names = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack',
                  12: 'Queen', 13: 'King'}
    bet = 100

    def __init__(self, money):
        self.money = money
        self.hand = []
        self.bust = False
        self.blackjack = False

    def get_card(self, d):
        # assert d is isinstance(object, Deck)
        self.hand.append(d.deal_one_card())

    def clear_hand(self):
        self.hand = []
        self.bust = False
        self.blackjack = False

    def get_total(self):
        total = 0
        aces = 0
        for c in self.hand:
            if c == 1:
                aces += 1
            elif c > 10:
                c = self.card_values[c]
            total += c
        for a in range(aces):
            if total + 10 <= 21:
                total += 10

        if total == 21:
            self.blackjack = True
        elif total > 21:
            self.bust = True

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
        if self.get_total() > 21:
            self.bust = True
        return self.bust

    def return_status_string(self, player_number):
        s = ""
        if player_number == 0:
            s += "\nDealer has all the money"
            s += "\nShowing: "
            for c in self.hand[1:]:
                s += self.card_names[c] + " "
        else:
            s += "\nPlayer " + str(player_number) + " has " + str(self.money) + " money"
            s += "\nContains: "
            for c in self.hand:
                s += self.card_names[c] + " "
            s += "for a total of\n"
            s += str(self.get_total()) + "\n"
        return s

    def dealer_moves(self, d):
        if self.bust:
            print("DEALER BUST")
        while not self.bust and self.get_total() < 17:
            self.get_card(d)
        s = ""
        print("\nDealer has the following cards:\n")
        for c in self.hand:
            s += self.card_names[c] + " "
        s += "for a total of \n" + str(self.get_total()) + "\n"
        print(s)


def get_positive_int_up_to(prompt, max):
    n = -1
    while n < 0:
        print("*" * 45)
        c = input(prompt + "\n")
        if c.isnumeric() and int(c) > 0 and int(c) <= max:
            n = int(c)
        elif c.isalpha():
            print("Please enter a number")
        elif c.isnumeric() and int(c) <= 0:
            print("Please enter a number higher than 0")
        elif c.isnumeric() and int(c) > max:
            print("Your number is too high, max selection is " + str(max))
        else:
            print("Invalid input, please try again")
    return n


def initialize_players(number, money):
    players = []
    # add extra player to act as the dealer
    # the dealer will be the first ([0]) object in the players list
    for x in range(number + 1):
        players.append(Player(money))
    return players


def initial_deal(players_list, deck):
    for p in players_list:
        p.get_card(deck)
    for p in players_list:
        p.get_card(deck)


def check_for_blackjack(players):
    for p in players:
        if p.get_total() == 21:
            p.blackjack = True


def ask_player_moves(players, d):
    # slice out first player (the dealer)
    for i, p in enumerate(players[1:]):
        print(p.return_status_string(i + 1))
        if p.blackjack:
            continue
        prompt = "Player " + str(i + 1) + ", what is your move? Choose 1 for stay, 2 to hit"
        move = get_positive_int_up_to(prompt, 2)
        while move != 1 and not p.bust and not p.blackjack:
            if move == 2:
                p.get_card(d)
            print(p.return_status_string(i + 1))
            if not p.bust:
                move = get_positive_int_up_to(prompt, 2)
        if p.bust:
            print("*" * 45 + "\nBUST BUST BUST BUST BUST BUST BUST BUST BUST\n" + "*" * 45)

def payout_clear_hands(players):
    winners = ""
    if players[0].bust:
        for i, p in enumerate(players[1:]):
            if not p.bust:
                winners += "Player " + str(i+1) + " won " + str(p.bet) + "\n"
                p.money += p.bet
            elif p.bust:
                p.money -= p.bet
    else:
        n = players[0].get_total()
        for i, p in enumerate(players[1:]):
            if p.get_total() > n and not p.bust:
                winners += "Player " + str(i+1) + " won " + str(p.bet) + "\n"
                p.money += 100
            elif p.get_total() == n and not p.bust:
                pass
            else:
                p.money -= 100
    print(winners)
    for p in players:
        p.clear_hand()


def print_everyone(players):
    for i, p in enumerate(players):
        print(p.return_status_string(i))

def main_loop():
    decks = get_positive_int_up_to("How many decks would you like to play with? Must be from 1 to 10", 10)
    seats = get_positive_int_up_to("How many seats would you like to play? Max of 5", 5)
    rounds = get_positive_int_up_to("\nHow many rounds would you like to play? Max of 100", 100)

    shoe = Deck(decks)
    players = initialize_players(seats, 1000)
    print("You are playing " + str(seats) + " seats with " + str(decks) + " decks for " + str(rounds) + " rounds.")

    for n in range(rounds):
        initial_deal(players, shoe)
        check_for_blackjack(players)
        if seats > 1:
            print_everyone(players)
        print(players[0].return_status_string(0))
        ask_player_moves(players, shoe)
        players[0].dealer_moves(shoe)
        payout_clear_hands(players)
        input("Press Enter to continue...")
        shoe.check_cards_remaining(len(players))
        print("*"*45+"\nNEW ROUND NEW ROUND NEW ROUND NEW ROUND NEW ROUND\n"+"*"*45)


main_loop()
#TODO implement strategies
#TODO implement betting