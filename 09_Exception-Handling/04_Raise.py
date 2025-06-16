x = int(input("Enter a level: ")) 

try:
    if (x<1 or x>10):
        raise ValueError
    else:
        print("Game is starting...") 
except ValueError:
    print("Game consists levels 1 to 10")   
