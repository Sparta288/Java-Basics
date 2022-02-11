answer = 5
guess = 0

while guess != answer:
    print("\nGuess a number between 1 and 10: ")
    guess = int(input())
    if guess == answer:
        print("Congrats you guessed correctly!")
    elif guess < answer:
        print("Your guess is to low. Guess higher")
    elif (guess > answer) and (guess <= 10):
        print("Your guess is to high. Guess lower. ")
    elif guess > 10:
        print("That number is out of range! ")


