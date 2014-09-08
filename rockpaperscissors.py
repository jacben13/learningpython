__author__ = 'Ben'
import random
computerwins = 0
playerwins = 0
ties = 0
def play():
    global computerwins
    global playerwins
    global ties
    bank = {1:"rock",2:"paper",3:"scissors"}
    playermove = askplayermove()
    computermove = getcomputermove()
    if determinewinner(playermove,computermove) == 1:
        playerwins += 1
        print("Player won with throwing "+bank[playermove]+" against "+bank[computermove])
    elif determinewinner(playermove,computermove) == 2:
        computerwins += 1
        print("Player lost with throwing "+bank[playermove]+" against "+bank[computermove])
    else:
        ties += 1
        print("Tie with both throwing "+bank[playermove])
    printscores()

def askplayermove():
    choice = 0
    while choice not in [1,2,3]:
        choice = input("Please choose 1 for rock, 2 for paper, and 3 for scissors")
        if choice.isnumeric():
            choice = int(choice)
        if choice in [1,2,3]:
            break
        print("That is not a valid choice, please try again!")
    return choice

def getcomputermove():
    return random.randint(1,3)

def determinewinner(p, c):
    if p-c == 0:
        return 3
    elif p-c == 1 or p-c ==-2:
        return 1
    elif p-c == 2 or p-c==-1:
        return 2
    else:
        return 3

def printscores():
    print("Match complete! Who will win the next round?")
    print("Standings are currently:\nPlayer: "+str(playerwins)+" matches \nComputer: "+str(computerwins) \
        + " matches\n" + str(ties) + " ties")

n = -1
while n < 0:
    c = input("How many matches would you like to play?")
    if c.isnumeric() and int(c)>0:
        n=int(c)
    elif c.isalpha():
        print("Please enter a number")
    elif c.isnumeric() and int(c)<=0:
        print("Please enter a number higher than 0")
    else:
        print("Invalid input, please try again")

for i in range(n):
    play()
print("Thanks for playing!")