__author__ = 'Ben'
import random

CARD_VALUES = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10}
CARD_NAMES = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack',
              12: 'Queen', 13: 'King'}


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
    broke = False
    double_bet = False
    bet = 100
    bust = False

    def __init__(self, money):
        self.money = money
        self.hand = []
        self.bust = False
        self.blackjack = False

    def get_card(self, d):
        # assert d is isinstance(object, Deck)
        if self.bet > self.money:
            self.bet = self.money
        self.hand.append(d.deal_one_card())

    def clear_hand(self):
        self.hand = []
        self.bust = False
        self.blackjack = False
        if self.double_bet:
            self.set_bet(int(self.bet / 2))
        self.double_bet = False

    def hard_hand(self):
        # Total up the hand, if we execute the part of the code that adds 10 more to the total for aces, we have a
        # soft hand, otherwise, we have a hard hand
        total = 0
        aces = 0
        hard = True
        for c in self.hand:
            if c == 1:
                aces += 1
            elif c > 10:
                c = CARD_VALUES[c]
            total += c
        # For aces, we already added 1, add an additional 10 if it doesn't go over 21
        for a in range(aces):
            if total + 10 <= 21:
                total += 10
                hard = False
        return hard

    def get_total(self):
        total = 0
        aces = 0
        for c in self.hand:
            if c == 1:
                aces += 1
            elif c > 10:
                c = CARD_VALUES[c]
            total += c
        # For aces, we already added 1, add an additional 10 if it doesn't go over 21
        for a in range(aces):
            if total + 10 <= 21:
                total += 10

        if total == 21 and len(self.hand) == 2:
            self.blackjack = True
        elif total > 21:
            self.bust = True

        return total

    def dealer_showing(self):
        return self.hand[1:]

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
                s += CARD_NAMES[c] + " "
        else:
            if self.broke:
                s += "\nPlayer " + str(player_number) + " is broke as a goat and taking up space!"
                return s
            s += "\nPlayer " + str(player_number) + " has " + str(self.money) + " money with a bet of " + str(self.bet)
            s += "\nContains: "
            for c in self.hand:
                s += CARD_NAMES[c] + " "
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
        if self.blackjack:
            print("DEALER BLACKJACK\n")
        for c in self.hand:
            s += CARD_NAMES[c] + " "
        s += "for a total of \n" + str(self.get_total()) + "\n"
        print(s)

    def set_bet(self, b):
        if b > self.money:
            self.bet = self.money
            return
        self.bet = b

    def double_down(self):
        self.double_bet = True
        self.set_bet(int(self.bet*2))



def get_positive_int_up_to(prompt, max_int):
    n = -1
    while n < 0:
        print("*" * 45)
        c = input(prompt + "\n")
        if c.isnumeric() and 0 < int(c) <= max_int:
            n = int(c)
        elif c.isalpha():
            print("Please enter a number")
        elif c.isnumeric() and int(c) <= 0:
            print("Please enter a number higher than 0")
        elif c.isnumeric() and int(c) > max_int:
            print("Your number is too high, max selection is " + str(max_int))
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
        if p.broke:
            continue
        p.get_card(deck)
    for p in players_list:
        if p.broke:
            continue
        p.get_card(deck)


def check_for_blackjack(players):
    for p in players:
        if p.get_total() == 21:
            p.blackjack = True


def ask_player_moves(players, d):
    # slice out first player (the dealer)
    for i, p in enumerate(players[1:]):
        print(p.return_status_string(i + 1))
        if p.blackjack or p.broke:
            continue
        prompt = "Player " + str(i + 1) + ", what is your move? Choose 1 for stay, 2 to hit, 3 for double down"
        print("Recommended move is " + recommend_move(p, players[0].dealer_showing()))
        move = get_positive_int_up_to(prompt, 3)
        while move != 1 and not p.bust and not p.blackjack:
            if move == 2:
                p.get_card(d)
            elif move == 3:
                p.double_down()
                p.get_card(d)
                print(p.return_status_string(i + 1))
                break
            print(p.return_status_string(i + 1))
            if not p.bust:
                print("Recommended move is " + recommend_move(p, players[0].dealer_showing()))
                move = get_positive_int_up_to(prompt, 3)
        if p.bust:
            print("*" * 45 + "\nBUST BUST BUST BUST BUST BUST BUST BUST BUST\n" + "*" * 45)


def recommend_move(player, dealer_card):
    # This function should return a string staying Hit, Stand, and any other implemented available moves
    # Recommendations are based on http://wizardofodds.com/games/blackjack/strategy/4-decks/
    h = "Hit (2)"
    s = "Stand (1)"
    d = "Double Down(3)"
    dealer_card = int(dealer_card[0])

    if player.hard_hand():
        if player.get_total() <= 8:
            return s
        elif player.get_total() == 9:
            if dealer_card in {3, 4, 5, 6} and not player.double_bet:
                return d
            else:
                return h
        elif player.get_total() == 10:
            if dealer_card >= 10 or dealer_card == 1 or player.double_bet:
                return h
            else:
                return d
        elif player.get_total() == 11:
            if dealer_card == 1 or player.double_bet:
                return h
            else:
                return d
        elif player.get_total() == 12:
            if dealer_card in {4, 5, 6}:
                return s
            else:
                return h
        elif player.get_total() in {13, 14, 15, 16}:
            if dealer_card == 1 or dealer_card >= 7:
                return h
            else:
                return s
        elif player.get_total() >= 17:
            return s
    else:
        if player.get_total() in {13, 14}:
            if not player.double_bet and dealer_card in {5, 6}:
                return d
            else:
                return h
        elif player.get_total() in {15, 16}:
            if not player.double_bet and dealer_card in {4, 5, 6}:
                return d
            else:
                return h
        elif player.get_total() == 17:
            if not player.double_bet and dealer_card in {3, 4, 5, 6}:
                return d
            else:
                return h
        elif player.get_total() == 18:
            if not player.double_bet and dealer_card in {3, 4, 5, 6}:
                return d
            elif dealer_card in {1, 9, 10}:
                return h
            else:
                return s
        elif player.get_total() >= 19:
            return s

    ''' This logic is for use when double down is not available
    if player.get_total() <= 11:
        return h
    elif player.hard_hand() and player.get_total() == 12 and dealer_card in {4, 5, 6}:
        return s
    elif player.hard_hand() and player.get_total() == 12:
        return h
    elif player.hard_hand() and player.get_total() in {13, 14, 15, 16} and dealer_card in {2, 3, 4, 5, 6}:
        return s
    elif player.hard_hand() and player.get_total() in {13, 14, 15, 16}:
        return h
    elif player.hard_hand() and player.get_total() >= 17:
        return s
    elif not player.hard_hand() and player.get_total() <= 17:
        return h
    elif not player.hard_hand() and player.get_total() == 18 and dealer_card in {1, 9, 10}:
        return h
    elif not player.hard_hand() and player.get_total() == 18:
        return s
    elif not player.hard_hand() and player.get_total() >= 19:
        return s
    '''

    return "F2IK"


def payout_clear_hands(players):
    winners = ""
    if players[0].bust:
        for i, p in enumerate(players[1:]):
            if p.blackjack and not p.bust:
                winners += "Player " + str(i + 1) + " won " + str(int(p.bet * 1.5)) + "\n"
                p.money += p.bet * 1.5
            elif not p.bust:
                winners += "Player " + str(i + 1) + " won " + str(p.bet) + "\n"
                p.money += p.bet
            elif p.bust:
                p.money -= p.bet
    else:
        n = players[0].get_total()
        for i, p in enumerate(players[1:]):
            if p.blackjack and not p.bust and not players[0].blackjack:
                winners += "Player " + str(i + 1) + " won " + str(int(p.bet * 1.5)) + "\n"
                p.money += p.bet * 1.5
            elif p.get_total() > n and not p.bust:
                winners += "Player " + str(i + 1) + " won " + str(p.bet) + "\n"
                p.money += p.bet
            elif p.get_total() == n and not p.bust:
                pass
            else:
                p.money -= p.bet
    print(winners)
    for p in players:
        p.clear_hand()


def print_everyone(players):
    for i, p in enumerate(players):
        print(p.return_status_string(i))


def print_final_score(players):
    s = "\n"
    for i, p in enumerate(players):
        s += "Player %d ended the game with %d money\n" % (i + 1, p.money)
    print(s)


def find_broke_players(players):
    broke_players = 1
    for i, p in enumerate(players[1:]):
        if p.money <= 0:
            p.broke = True
            print("Player " + str(i + 1) + " is broke as a goat!")
            broke_players += 1
    if len(players) <= broke_players:
        print("Everyone is out of money!")
        exit()


def ask_to_continue_or_change_bet(players):
    while True:
        try:
            i = int(input("Hit enter to continue or input a player number to change bet\n"))
        except ValueError:
            return
        if 0 < i < len(players):
            new_bet = get_positive_int_up_to("What is the new bet for player " + str(i), players[i].money)
            players[i].set_bet(new_bet)
        else:
            print("Try inputting a player number instead")


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
        find_broke_players(players)
        ask_to_continue_or_change_bet(players)
        shoe.check_cards_remaining(len(players))
        if n != rounds - 1:
            print("*" * 45 + "\nNEW ROUND NEW ROUND NEW ROUND NEW ROUND NEW ROUND\n" + "*" * 45)
    print_final_score(players[1:])


main_loop()

#TODO add double down to recommended moves