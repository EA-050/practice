import random

target = random.randint(1,1000)

while True:
    choice = int(input("enter a number: "))
    if choice == target:
        print("well done you guessed right")
        break
    elif choice > target:
        print("you guess is too high try again")
    else:
        print("you guessed too low try again")

