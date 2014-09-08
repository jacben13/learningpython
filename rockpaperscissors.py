__author__ = 'Ben'
import random

computerwins = 0
playerwins = 0
ties = 0
spockdeaths = 0


def play():
    global computerwins
    global playerwins
    global ties
    bank = {1: "rock", 2: "paper", 3: "scissors"}
    playermove = askplayermove()
    computermove = getcomputermove()
    if determinewinner(playermove, computermove) == 1:
        playerwins += 1
        print("Player won with throwing " + bank[playermove] + " against " + bank[computermove])
    elif determinewinner(playermove, computermove) == 2:
        computerwins += 1
        print("Player lost with throwing " + bank[playermove] + " against " + bank[computermove])
    else:
        ties += 1
        print("Tie with both throwing " + bank[playermove])


def playrpsls():
    global computerwins
    global playerwins
    global ties
    global spockdeaths
    bank = {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "Spock"}
    playermove = askplayermoverpsls()
    computermove = getcomputermoverpsls()
    if determinewinnerrpsls(playermove, computermove) == 1:
        if computermove == 5:
            spockdeaths += 1
        playerwins += 1
        print("Player won with throwing " + bank[playermove] + " against " + bank[computermove])
        print(winhow(playermove, computermove))
    elif determinewinnerrpsls(playermove, computermove) == 2:
        if playermove == 5:
            spockdeaths += 1
        computerwins += 1
        print("Player lost with throwing " + bank[playermove] + " against " + bank[computermove])
        print(winhow(computermove, playermove))
    else:
        ties += 1
        print("Tie with both throwing " + bank[playermove])


def askplayermove():
    choice = 0
    while choice not in [1, 2, 3]:
        choice = input("Please choose 1 for rock, 2 for paper, and 3 for scissors")
        if choice.isnumeric():
            choice = int(choice)
        if choice in [1, 2, 3]:
            break
        print("That is not a valid choice, please try again!")
    return choice


def askplayermoverpsls():
    return getpositiveintupto("Please choose 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for Spock", 5)


def getcomputermove():
    return random.randint(1, 3)


def getcomputermoverpsls():
    return random.randint(1, 5)


def determinewinner(p, c):
    if p - c == 0:
        return 3
    elif p - c == 1 or p - c == -2:
        return 1
    elif p - c == 2 or p - c == -1:
        return 2
    else:
        return 3


def determinewinnerrpsls(p, c):
    # Convention for the truth table is 3 is a tie, 1 indicates column player won and 2 indicates row player won
    wintable = [["", "Rock", "Paper", "Scissors", "Lizard", "Spock"],
                ["Rock", 3, 2, 1, 1, 2],
                ["Paper", 1, 3, 2, 2, 1],
                ["Scissors", 2, 1, 3, 1, 2],
                ["Lizard", 2, 1, 2, 3, 1],
                ["Spock", 1, 2, 1, 2, 3]]
    if p - c == 0:
        return 3
    else:
        return wintable[p][c]


def winhow(p, c):
    global spockdeaths
    bank = {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "Spock"}
    verbtable = [["", "Rock", "Paper", "Scissors", "Lizard", "Spock"],
                 ["Rock", 3, 2, "crushes", "crushes", 2],
                 ["Paper", "covers", 3, 2, 2, "disproves"],
                 ["Scissors", 2, "cuts", 3, "decapitates", 2],
                 ["Lizard", 2, "eats", 2, 3, "poisons"],
                 ["Spock", "vaporizes", 2, "smashes", 2, 3]]
    return bank[p] + " " + verbtable[p][c] + " " + bank[c] + "\nSpock has died " + str(spockdeaths) + " times."


def printscores():
    line = "=" * 45
    print("Match complete! Who will win the next round?")
    print(line)
    print("Standings are currently:\nPlayer: " + str(playerwins) + " matches \nComputer: " + str(computerwins) \
          + " matches\n" + str(ties) + " ties")
    print(line)


def clearscreen():
    print("\n" * 50)


def getpositiveintupto(prompt, max):
    n = -1
    while n < 0:
        print("*" * 45)
        c = input(prompt)
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


n = getpositiveintupto("How many matches would you like to play?", 20)
game = getpositiveintupto("Pick 1 for regular rock paper scissors, pick 2 for rock paper scissors lizard spock:", 2)

for i in range(n):
    if game == 1:
        play()
    elif game == 2:
        playrpsls()
    printscores()
print("Thanks for playing!")