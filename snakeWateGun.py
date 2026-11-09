import random

# Dictionary
youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Score
user_score = 0
computer_score = 0

rounds = 5

print("\n===== SNAKE WATER GUN GAME =====")
print("s = Snake")
print("w = Water")
print("g = Gun")

# Game Loop
for i in range(1, rounds + 1):

    print(f"\n========== ROUND {i} ==========")

    while True:

        youstr = input("Enter your choice (s/w/g): ").lower()

        if youstr in youDict:
            break

        print("Invalid Choice! Please enter s, w or g.")

    # Computer Choice
    computer = random.choice([1, -1, 0])

    # User Choice
    you = youDict[youstr]

    print("\nYou chose:", reverseDict[you])
    print("Computer chose:", reverseDict[computer])

    # Winner Logic
    if computer == you:
        print("\nIt's a Draw!")

    elif (computer == -1 and you == 1) or \
         (computer == 1 and you == 0) or \
         (computer == 0 and you == -1):

        print("\nCongratulations! You Win!")
        user_score += 1

    else:
        print("\nComputer Wins!")
        computer_score += 1

    # Display Score
    print("\n---------- SCORE ----------")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)


# Final Result
print("\n======= FINAL RESULT =======")

print("Your Final Score:", user_score)
print("Computer Final Score:", computer_score)

if user_score > computer_score:
    print("\nCongratulations! You are the Champion!")

elif computer_score > user_score:
    print("\nComputer is the Champion!")

else:
    print("\nMatch Draw!")

print("\nThanks for Playing!")