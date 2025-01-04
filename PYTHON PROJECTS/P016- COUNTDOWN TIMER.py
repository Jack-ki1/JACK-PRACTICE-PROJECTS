import time

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{ :02d}: {:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep
        t -= 1
        
    print('Fire in thne hole!!')
    
    t = input("Enter the time in seconds")
    
countdown(int(t))