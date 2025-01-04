import random #random library allows the program to generate random numbers

random_number = random.randint(1,10)#random_number stores variable between 1 and 10

while True:
    user_number = int(input("Pick a number between 1 and 10: "))#input() captures input as a string then int() convertsthe string into an integer
    
    if user_number < random_number:#if user_number is less than random_number u have to put in a bigger number
        print("It's bigger than that")
        continue
    elif user_number > random_number:#if user_number is greater than random_number u have to put in a smaller number
        print("It's smaller than that")
        continue
    else:
        print("You have guessed it!")
        break
