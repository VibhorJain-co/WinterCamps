# Scissors cut paper
# Paper covers rock
# Rock crushes lizard
# Lizard poisons Spock
# Spock smashes scissors
# Scissors decapitate lizard
# Lizard eats paper
# Paper disproves Spock
# Spock vaporizes rock
# Rock breaks scissors

import random

choices = {
    0:"ROCK",
    1:"PAPER",
    2:"SCISSOR",
    3:"SPOCK",
    4:"LIZARD"
}

def Game():
    BotChoice = random.randint(0,4)
    UserChoice = int(input("Choose your choice (0 to 4): "))

    if(UserChoice == -1):
        print("EXITED\n\n\n")
        return 1

    diff = abs(BotChoice-UserChoice)
    if(diff == 0):
        print("Tie Game")
        #return 0;
    elif(diff%2 != 0):
        if((BotChoice + diff)%5 == UserChoice): # *you can ALWAYS use MODULUS to implement cyclicity in such cases, whehere values are assigned numbers*
            print("You Win")
        else:
            print("You Lose")
    else:
        if((BotChoice - diff)%5 == UserChoice):
            print("You Win")
        else:
            print("You Lose")

    print(f"CC:{choices.get(BotChoice)}  UC:{choices.get(UserChoice)}")
    return 0

stop = 0
while(not stop):
    stop = Game()
    print()