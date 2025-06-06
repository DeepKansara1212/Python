import random

random_no = random.randint(1, 100)
# print(random_no)

tries = 0

while True:
    guess = int(input("Guess the number between 1 to 100: "))

    # tries += 1 

    if random_no == guess:
        tries += 1
        print("Congratualtion, You Guessed it right.")
        break
    elif guess > random_no:
        tries += 1
        print("Too High")
    elif guess < random_no:
        tries += 1
        print("Too low")
    else: 
        print("Invalid Number. Enter the number between 1 to 100.") 