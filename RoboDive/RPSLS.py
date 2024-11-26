# spock > rock,scissors
# lizard > spock,paper
# rock > lizard,scissors
# paper > rock,spock
# scissors > paper,lizard

import random
choices = ["rock","paper","scissor","lizard","spock"]

wins = {
        "rock": ["lizard","scissors"],
        "paper": ["rock","spock"],
        "scissor": ["paper","lizard"],
        "lizard": ["spock","paper"],
        "spock": ["rock","scissors"]
        }
BotChoice = random.choice(choices)
UserChoice = input("Choose your choice: ")

