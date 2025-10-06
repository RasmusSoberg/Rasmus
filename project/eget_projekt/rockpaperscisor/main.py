import random


winning_rules = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}


score = {"wins": 0, "losses": 0, "draws": 0}

def play_rps(player_choice, bot_choice):
    player_choice = player_choice.lower()
    bot_choice = bot_choice.lower()
    
    if player_choice == bot_choice:
        print(f"Both chose {player_choice}. It's a draw!")
        score["draws"] += 1
    elif winning_rules[player_choice] == bot_choice:
        print(f"You chose {player_choice}, bot chose {bot_choice}. You win!")
        score["wins"] += 1
    else:
        print(f"You chose {player_choice}, bot chose {bot_choice}. You lose!")
        score["losses"] += 1


options = ["rock", "paper", "scissors"]

choice = input("Choose rock, paper, or scissors (or type 'quit' to stop): ")
while choice.lower() != "quit":
    botPick = random.choice(options)
    play_rps(choice, botPick)
    print(f"Score: {score}")
    
    choice = input("Choose: ")






