from tkinter import *
from tkinter import messagebox
import random


#create window 

window = Tk()
window.title("DiceGame21")
window.geometry("400x400")
window.resizable(False, False)
window.configure(borderwidth=5, background="green")

#initiate game variables
houseValue = 0
userValue = 0

# ======================================== commands =====================================================]
#help/info box
def help():
    messagebox.showinfo("Help", "Dicegame based on blackjack. Pressing Play rolls 3 dices and adds up yours and the House's numbers, press Hit to roll again, press Stick to keep your current value. The aim is to get closest to 21 without rolling over. Anyone who rolls over 21 goes bust and loses! If the House rolls the same as you, they automatically win (House advantage). Good luck!")

#method to print gametext to main label
def printText(update):
    main.configure(text = update)

#method for initiating the game, rolls 3 dice and sums the score
def initialRole(baseScore):
        for i in range(3):
            baseScore += random.randint(1,6)
        return baseScore

#to initiate the game once player starts/restarts
def gameStart():
    global userValue 
    global houseValue 
    userValue = initialRole(userValue)
    houseValue = initialRole(houseValue)
    playButton.configure(state="disabled")
    hitButton.configure(state="active")
    stickButton.configure(state="active")
    return f"You've rolled {userValue}. The House has rolled {houseValue}. \nHit or stick?"

#hit - main method for gameplay
def hit(score):
    score += random.randint(1,6)
    return int(score)

#updates the value when a user hits and prints to the console
def userHitUpdate():
    global userValue
    userValue = hit(userValue)
    if userValue > 21:
        hitButton.configure(state="disabled")
        stickButton.configure(state="disabled")
        messagebox.showinfo("Bust!", f"You hit for {userValue}. You lose!")
        return f"You hit for {userValue} and went bust!"
    else:
        return f"You hit for {userValue}. The house has rolled {houseValue}. \nHit or stick?"

#updates the value when the House hits and prints to the console
def houseHitUpdate():
    global houseValue
    houseValue=hit(houseValue)
    return houseValue

#stick method saves the users current score, initiates the House's game logic 
def stick():
    hitButton.configure(state="disabled")
    global houseValue
    while int(houseValue) < int(userValue) and int(houseValue) < 21:
        houseValue = houseHitUpdate()
        if houseValue > 21:
            main.configure(text= f"You rolled {userValue}. The House hit for {houseValue} and went bust!")
        else:
            main.configure(text= f"You rolled {userValue}. The House has hit for {houseValue}.")
    checkScores()

#method to compare player score to house score
def checkScores():
    global userValue
    global houseValue
    if (((21-userValue) < (21-houseValue)) and userValue < 21) or houseValue > 21:
        messagebox.showinfo("Winner", "You win!")
    else:
        messagebox.showinfo("Loser", "You lose!")

#replay, resets game
def replay():
    global userValue
    global houseValue
    userValue = 0
    houseValue = 0
    printText(gameStart())
    
# ================================ GUI code =======================================================

#main game box; place is on a separate line so it can be configured. 
main = Label(window, text=" ", height=9, width=52)
main.place(x=10,y=90)

#instruction messagebox/help button
helpButton = Button(window, text="?", font=("Helvetica", 7, "bold"), width=1, height=1, command=help).place(x=375,y=0)

#instruction label
startLabel = Label(window, text="Press Play to begin", font=("Ariel")).pack()

#start button - starts the game loop; command is passed as a lambda expression to stop it from executing upon loading; separate line place to make callable
playButton = Button(window, text="Play", width=10, height=1, font=("Helvetica", 10, "bold"), command=lambda:printText(gameStart()))
playButton.place(x=150,y=50)

#hit button
hitButton = Button(window, text="Hit", width=10, height=2, font=("Helvetica", 20, "bold"), state="disabled", command=lambda:printText(userHitUpdate()))
hitButton.place(x=10,y=240)

#stick button
stickButton = Button(window, text="Stick", width=10, height=2, font=("Helvetica", 20, "bold"), state="disabled", command=lambda:stick())
stickButton.place(x=200, y=240)

#restart button
restartButton = Button(window, text="Replay", width=7, height=1, command=lambda:replay())
restartButton.place(x=130,y=350)

#exit button, lambda quit
exitButton = Button(window, text="Quit", width=7, height=1, command=lambda:window.quit()).place(x=200,y=350)

window.mainloop()
