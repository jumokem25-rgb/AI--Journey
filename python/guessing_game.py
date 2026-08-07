secret_number = 7

guess = int(input("Guess a number from 1 to 10: "))

if guess == secret_number:
    print("Correct you guessed it!")
elif guess < secret_number:
     print("Too low! Try again.")
else:
    print("Too high! Try again.")
