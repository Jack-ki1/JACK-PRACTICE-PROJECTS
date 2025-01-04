import datetime

user_input = input("Enter your birth year YYYY-MM-DD: ")

birthday = datetime.datetime.strptime(user_input, "%Y-%m-%d")
today = datetime.datetime.now()

age = (
    today.year
    -birthday.year
    -((today.month, today.day) < (birthday.month, birthday.day))
        
)

print(age)


