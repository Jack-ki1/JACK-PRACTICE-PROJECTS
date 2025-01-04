dataset = {"ivan":"123ivan", "dragon":"456dragon"}

username = input("Enter your username: ")

if username in dataset:
    password = input("Enter your password: ")
    
    while password != dataset[username]:
        password = input("Enter your passeword again: ")
    print("logged in")
else:
    print("invalid username")