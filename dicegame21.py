import random
"""
Dicegame based on blackjack, the game is initiated by rolling a dice three times and summating the values for the player and the House. 
The player then has a choice to make, either to hit (roll another dice) or to stick with the current number.
The aim is to get 21 or as close to it as possible, and the winner is the player who gets closer to 21 without going over.
Anyone who rolls over a total of 21 goes 'bust' and loses; if it is a tie, then the House wins (house advantage).
When a player 'sticks' with their chioce, the house will continue to hit until it fulfils the winning criteria, i.e. if it has a value that
is less than the player's value and is still less than 21, it will continue to hit, even at the risk of going bust.

"""
"""
TODO, create GUI for program and implement other features e.g. split.
TODO, ask if player wants to play again rather than quit out of.
"""
#initiate the two starting values with global variables
houseValue = 0
userValue = 0

#command - start - initiates the game by adding 3 random numbers between 1 and 6 
def start(score):
    for i in range(3):
        score += random.randint(1,6)
    return score

#command - hit - increases the score by a random int between 1 and 6
def hit(score):
    score += random.randint(1,6)
    return int(score)

#compares scores at the end to dictate winner, userscore automatically loses if hits over 21 so no extra conditionals needed 
def compareScores(userScore, houseScore):
    if (((21-userScore) < (21-houseScore)) and houseScore < 21) or houseScore > 21:
        print("You win!")
        print("===================================================")
    else:
        print("You lose!")
        print("===================================================")


#game engine/logic - 3 random numbers between 1 and 6, added (startNumber), ask user to hit/stick. House will also have 3 random numbers
#house logic, to keep hitting until number fulfils winning criteria. 
"""
Winning criteria for user: player score must be under 21 but score difference between 21 and player score must be smaller than the difference
between the House score and 21. If anyone hits for above 21, they lose. 
"""
game = True
userValue = start(userValue)
houseValue = start(houseValue)
while game:
    print("===================================================" )
    print(f"<> Your score is {userValue}, the House currently has {houseValue}. <> \n \n        +          Hit or stick?           + ")
    print("===================================================")
    user = input()
    if user.lower() in ("hit", "stick"):
        if user == "hit":
            print("===================================================")
            userValue = hit(userValue)
            print(f"You hit for {userValue}.".center(52))
            if userValue > 21:
                print("Bust! You lose!".center(50))
                print("===================================================")
                break
            print("===================================================")
        elif user == "stick":
            #if user chooses to stick, House game logic initiates
            print("===================================================")
            while houseValue < 21 and houseValue < userValue:
                houseValue = hit(houseValue)
                print(f"House hits and gets {houseValue}!")
                if houseValue > 21:
                    print(f"House hits for {houseValue}. Bust! You win!")
            print("===================================================")
            compareScores(userValue, houseValue)
            break
    else:
        #to only accept hit or stick as a user input
        print("\nPlease enter 'hit' or 'stick'.\n")