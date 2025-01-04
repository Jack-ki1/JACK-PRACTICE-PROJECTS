import random

def picks():
    options= ["rock", "paper", "scissors"]
    
    user_pick = input("your pick from options: ")
    ai_pick = random.choice(options)
    
    print(f"computer pick :{ai_pick}")
    
    return user_pick, ai_pick

def play():
    while True:
        user_pick, ai_pick =picks()
        
        if user_pick == ai_pick:
            print("Draw!")
        elif user_pick == "rock" and ai_pick == "paper" or \
            user_pick == "paper" and ai_pick == "rock" or \
            user_pick== "scissors" and ai_pick == "paper":
            print("you win")
        else:
            print("computer wins")
