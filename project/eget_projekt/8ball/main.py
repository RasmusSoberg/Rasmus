import random
import time
import sys







responseList = [
        "Yes",
        "No",
        "Maybe",
        "Ask again later",
        "Signs point to yes",
        "Without a doubt",
        "Don't count on it",
        "Very doubtful",
        "Outlook good",
        "Yes definetly",
        "It is certain",
        "As I see it, yes",
        "You may rely on it",
        "It is decidedly so",
        "Better not tell you now",
        "Cannot predict right now",
        "Concentrate and ask again",
        "My reply is no",
        "My sources say no",
        "Reply hazy, try again",
        "Definetly no",
    ]

print("Welcome to the Magic 8-Ball")

while True:
    question = input("\nAsk your question (or type 'quit' to exit): ")

    if question.lower() == "quit":
        print ("Goodbye!")
        break

    print("Thinking", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print()

    answer = random.choice(responseList)
    print(answer)
