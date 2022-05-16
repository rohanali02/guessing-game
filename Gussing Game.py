import random
import time
import os

res = "y"


def clrscr():
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')


def guess():
    n = random.randint(1, 4)
    if n == 1:
        time.sleep(1.5)
        print("\nIt is an animal, Who is furry and love to eat fish")
        time.sleep(1.5)
        answer = input("\nEnter the name of animal: ")
        answer = answer.lower()
        if answer == 'cat':
            print(name + "! The answer is correct")
        else:
            print(name + "! Its a wrong answer")
    elif n == 2:
        time.sleep(1.5)
        print("\nIt is an animal, Who is furry and love to eat Banana")
        time.sleep(1.5)
        answer = input("\nEnter the name of animal: ")
        answer = answer.lower()
        if answer == "monkey":
            print(name + "! The answer is correct")
        else:
            print(name + "! Its a wrong answer")

    elif n == 3:
        time.sleep(1.5)
        print("\nIt is an animal, Who is furry and have strips on body and love to eat flesh")
        time.sleep(1.5)
        answer = input("\nEnter the name of animal: ")
        answer = answer.lower()
        if answer == "tiger":
            print(name + "! The answer is correct")
        else:
            print(name + "! Its a wrong answer")
    elif n == 4:
        time.sleep(1.5)
        print("\nIt is an animal, Who is furry and king of jungle and love to eat flesh")
        time.sleep(1.5)
        answer = input("\nEnter the name of animal: ")
        answer = answer.lower()
        if answer == "lion":
            print(name + "! The answer is correct")
        else:
            print(name + "! Its a wrong answer")


name = input("\nEnter Your name: ")
print('Hi '+ name + "! Welcome to the Animal name guessing game")
time.sleep(1.0)
ans = input("\nAre you ready to play - Yes/no: ")
ans = ans.lower()
if ans == "yes":
    guess()
elif ans == "no":
    quit()

else:
    print("Enter Yes or No Only")

while (res):
    if res.lower() == "y":
        res = str(input("\nDo you want to try again? "))
        clrscr()
        guess()
        print()
    else:
        quit()
