import random

# Get info from user whether they want to play Player1 vs. Player2 or Player1 vs. AI
gameplay = input("Would you like to play \n \t Player1 vs Player2? (1) \n \t Player1 \
vs AI? (2)\n-->")
#Changed your triple quotes to regular quotes since you already escaped the new line
#removed option 3 since its not required in your assignment

#Get input for starting number of sticks, if input is invalid prompt until valid
sticksint = int(0)
sticksremaining = int(0)
while gameplay == '1' or gameplay == '2':
    sticksstr = input("Please enter the number of sticks to begin with (10-50) -->")
    sticksint = int(sticksstr)
    if sticksint >= 10 and sticksint <= 50:
        print("Okay, there are", sticksint, "sticks in the pile.")
        break
    elif sticksint < 10 or sticksint > 50:  #prompt again if invalid
        print("You must enter a value between 10 and 50.")

#Game startup if user chooses player1 vs. player2
player2 = int(0)
player1 = int(0)
player1str = int(0)
player2str = int(0)
while gameplay == '1' and sticksint >= 3: #added second condition
    while True: #needed another nested loop for Player 1's input
        player1str = input("Player 1 enter the number of sticks to take: (1-3) -->")
        player1 = int(player1str) #changed to variable to player1str, fyi this crashes with null input
        if player1 >= 1 and player1 <= 3:
            print("Player 1 took", player1, "sticks.")
            sticksint -= player1
            print("There are", sticksint, "sticks left in the pile.")
            break  #escape if valid
        elif player1 < 1 or player1 > 3:  #prompt again if invalid
            print("You must pick an appropriate number of sticks to take. (1-3)")
    while True: # this needs to be a nested loop it looks like
        player2str = input("Player 2 enter the number of sticks to take: (1-3) -->")
        player2 = int(player2str)
        if player2 >= 1 and player2 <= 3:
            print("Player 2 took", player2, "sticks.")
            sticksint -= player2
            print("There are", sticksint, "sticks left in the pile.")
            break  #escape if valid
        elif player2 < 1 or player2 > 3:  #prompt again if invalid
            print("You must pick an appropriate number of sticks to take. (1-3)")

#game startup if user chooses AI
ai = int(0)
while gameplay == '2' and sticksint >= 3:
    player1str == input("Player 1 enter the number of sticks to take: (1-3) -->")
    player1 = int(player1str)
    if player1 >= 1 and player1 <= 3:
        print("Player 1 took", player1, "sticks.")
        sticksint -= player1
        print("There are", sticksint, "sticks left in the pile.")
        break
    elif print("You must pick an appropriate number of sticks to take. (1-3)"): #added a colon here
        continue #added continue here to redirect loop correctly
    ai = random.randint(1, 3) #changed equality comparison operator to assignment operator (you had ==, needs =)
    print("AI took", ai, "sticks.")
    sticksint -= ai
    print("There are", sticksint, "sticks left in the pile.")

#game winding down, only one option when sticks are down to 2
if sticksint == 2: #lines following here needed a tab and changed to an if
    player1str == input("Player 1 enter the number of sticks to take (1) -->") #you need to verify input here
    player1 = int(player1str)
if player1 == 1:
    print("Congrats winner!")
    # break This break doesn't do anything since it's outside of a loop
elif player1 != 1: # added a colon
    print("You must pick an appropriate number of sticks to take. (1)")  #game startup if user chooses quit
while gameplay == '3':
    exit() #changed to exit

#All in all, your code needed some cleanup, I commented all changes.
#A big problem right now is your game still does end correctly, I didn't bother to fix it because you need
#to do the work.  I'd recommend creating a new variable to keep track of which player's turn it is
#and then handle each case after the main game play loops like you already setup
#also, the AI's turn in your AI mode needs to be in its own loop just like the player vs player game