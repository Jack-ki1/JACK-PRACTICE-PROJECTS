attempts = 5

while attempts > 0:
    print(f"\n you have {attempts} attempts left.")
    
    name = input("what is your name? ")
    print(f"{name}, welcome to this wonderful adventure")

    option = input("first you have to choose a direction (north, south, east, west)? ")
    if option == "north":
            decision = input("you now enter a forest, and you see a certain old house \
            1.you walk to the house \
            2.you avoid the house \
                choose(1 or 2)? ")
            if decision == "1":
                    print("you see the treasure")
                    print("you win")
            elif decision == "2":
                    print("you get lost !!")
                    print("you lose")
            else:
                print(" sorry  wrong")
    
    if option == "south":
        answer = input("you can now either go left or right? ")
        if answer == "left":
            print("you ran back hence you lose")
        elif answer == "right" :
            print(" you see the treasure ")
            print(" you win")
        else:
            print("invalid option")
            break
        
    if option == "west":
        print("a lion catches you and eats you, you lose")
    
    if option == "east":
        print("you get lost")
        
    else:
        print("not valid option")
        
    attempts -= 1
    
    if attempts > 0 :  
        play_again = input("do you want to continue playing (yes or no)? ")
        if play_again != "yes":
            print(" thank you for you time have a nice day")
            break
            
    else:
        ("your attempts have ran out")
        break
            
            