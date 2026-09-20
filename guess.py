import random
num =random.randint(1,10)

tries=0
while True:
    guess =int (input("Guess the number between 1 to 10 -> "))
    if guess==num:
        print("you guessed it right")
        break
    else:
        print("try again")
        tries+=1
        print(f"You have {10-tries} tries left")
        if tries >= 10:
            print("You have exhausted all your tries")
            break
        