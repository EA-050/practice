import random

target = 0
level = input("easy or hard: ")
if level == "easy":
    target = random.randint(1,50)
elif level == "hard":
    target = random.randint(1,1000)
hashmap = {"easy": "1 - 50" , "hard" : "1 - 1000"}
while True:
    choice = int(input(f"enter a number {hashmap[level]} : "))
    if choice == target:
        print("well done you guessed right")
        break
    elif choice > target:
        print("you guess is too high try again")
    else:
        print("you guessed too low try again")

