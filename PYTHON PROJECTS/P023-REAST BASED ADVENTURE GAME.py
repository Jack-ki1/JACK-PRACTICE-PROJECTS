name = input ("please enter your name? ")
print("welcome, "+ name + " to this new adventure")

MAX_ATTEMPTS = 4
def intro():
    print("you can go north, south, east or west.")
    move(0)
    
def move(attempts):
    if attempts >= MAX_ATTEMPTS:
        print("you've reached max attempts. game over!")
        return
    
    direction = input("which way do you want to go? ")
    if direction == "north":
        north(attempts + 1)
    elif direction == "south":
        south(attempts + 1)
    elif direction == "east":
        east(attempts + 1)
    elif direction == "west":
        west( attempts + 1)
    else:
        print("invalid option")
        move(attempts)
    
        
def north(attempts):
    print("you fell into a river")
    print("you lose")
    move(attempts)

def south(attempts):
    print(" a lion kills you")
    print("you lose")
    move(attempts)
        
def east(attempts):
    choice = input(" you see two roads, you can either go left or right? ")
    if choice != "left":
        print("you lose")
    else:
        print(f"{name}, you win")
    move(attempts)
          
def west(attempts):
    option = input("you see an old man, \
                1.you can walk to the old man \
                2.you can avoid him \
                choose (either 1 or 2)? ")
    if option == "1":
        print("the old man gifts  you and advices you on what to do next")
        print(f" {name}, you win")
    else:
        print("you get lost")
        print(f" {name}, you lose")
    move(attempts)
        
intro()