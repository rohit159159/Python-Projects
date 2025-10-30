import random

print("🎯 Welcome to the Guess the Number Game!")
print("Choose a number between 1 and 100...")
print("You have only 7 attempts to guess it correctly!\n")

secret_number = random.randint(1, 100)
attempts = 7

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try a higher number.")
    else:
        print("📈 Too high! Try a lower number.")

    attempts -= 1
    print(f"Attempts left: {attempts}\n")

if attempts == 0:
    print(f"😢 Game Over! The number was {secret_number}.")  