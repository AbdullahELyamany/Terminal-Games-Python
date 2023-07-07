# This game is to guess a number from 1 to x
# Created by Abdullah Al-Yamani

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'\n\033[;32;mGuess a number between 1 and {x}: '))
        if guess < random_number:
            print('\033[;31;mSorry, guess again. Too low.')
        elif guess > random_number:
            print('\033[;31;mSorry, guess again. Too high.')

    print(f'\n\033[;36;mYay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    print(f"""\n\n\033[;36;mChoose a number in your mind between 1 and {x}.
If the computer guesses the number you chose, then you will be press (c).\n""")
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'\033[;32;mIs {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'\n\033[;36;mYay! The computer guessed your number, {guess}, correctly!')



print("\033[;36;mThis Game To Guess a Number From 1 to x\n")

try:
    high_num = int(input("\033[;32;mEnter Number (x): "))
except:
    print("\n\033[;31;mPlease Enter Only Numbers!!")
    high_num = int(input("\033[;32;mEnter Number: "))

print("""\033[;39;m
Do you want to
          [1] Guess the Number
          [2] Computer Guesses the Number
""")

num = input("\033[;32;mEnter 1 or 2 : ")

while True:
    if num == '1':
        guess(high_num)
        break
    elif num == '2':
        computer_guess(high_num)
        break
    else:
        print("\n\033[;31;mPlease Enter 1 or 2")
        num = input("\033[;32;mEnter 1 or 2 : ")

