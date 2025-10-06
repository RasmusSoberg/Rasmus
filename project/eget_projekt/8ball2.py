import random

winning_rules = {
    "scissors": "paper",
    "paper": "rock",
    "rock": "scissors",
}



score = {"wins":0, "losses": 0, "draws":0}


def play_rps(playerChoice, botChoice):
    if playerChoice == botChoice:
        print(f"Both picked {playerChoice} it's a draw")
        score ["draws"] += 1
    elif winning_rules[playerChoice] == botChoice:
        print(f"Bot picked {botChoice}. You win")
        score ["wins"] +=1
    else:
        print(f"Bot picked {botChoice}. You loose")
        score ["losses"] +=1

options = ["rock", "paper", "scissors"]

choice = input("PICK OR TYPE 'quit' TO EXIT: ")

while choice != "quit":
    if choice not in options:
        print("not an option")
    else:
    
        botPick = random.choice(options)
        play_rps(choice,botPick)
        print(score)
    

    if score ["wins"] == 5:
        print (" YOU WIN ")
        break
    elif score ["losses"] == 5:
        print ("YOU LOOSE")
        break
    choice = input ("PICK: ")
