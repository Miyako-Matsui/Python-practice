import random

print("Let's start a number guessing game.")
print("The answer is in the range of 1 to 10.")

answer = random.randrange(start=1, stop=10)
guess = int(input("Please enter your guess: "))

tries = 1

while guess != answer:
    if (guess > answer):
      print("Hint: Smaller number!")
    else:
      print("Hint: Biger number!")

    tries += 1
    guess = int(input("Please enter your guess:"))


print("Congratulations! The answer is " +  str(answer) + ".")
print(str(tries) + " tries.")