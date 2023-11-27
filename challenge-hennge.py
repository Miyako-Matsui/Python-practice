# Description
# We want you to calculate the sum of squares of given integers, excluding any negatives.
# The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
# Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
# For each test case, calculate the sum of squares of the integers, excluding any negatives, and print the calculated sum in the output.
# Note: There should be no output until all the input has been received.
# Note 2: Do not put blank lines between test cases solutions.
# Note 3: Take input from standard input, and output to standard output.






# import random

# print("Let's start a number guessing game.")
# print("The answer is in the range of 1 to 10.")

# answer = random.randrange(start=1, stop=10)
# guess = int(input("Please enter your guess: "))

# tries = 1

# while guess != answer:
#     if (guess > answer):
#       print("Hint: Smaller number!")
#     else:
#       print("Hint: Bigger number!")

#     tries += 1
#     guess = int(input("Please enter your guess:"))


# print("Congratulations! The answer is " +  str(answer) + ".")
# print(str(tries) + " tries.")

# import random 

# def test(testCase):
#     if testCase == 0:
#         return
#     testCaseInteger = random.randrange(start=1, stop=10)
#     print(testCaseInteger)

#     #list使えないってことはこれダメだと思うんだよねそれで数字が
#     #10じゃなくてマイナスからだからここもやり直しなんだけど
    
#     random_numbers = list(map(random.randrange, [10] * testCaseInteger))
#     print(*random_numbers)

#     test(testCase - 1) 

# def generate_random():
#     testCase = random.randrange(start=1, stop=5)
#     print(testCase)

#     test(testCase)

# generate_random()


import random

def generate_random_numbers(test_case_integer):
    random_number = random.randint(1, test_case_integer)
    print(random_number)
    random_numbers = map(lambda _: random.randint(-5, 5), range(random_number))
    return tuple(random_numbers)

result = generate_random_numbers(10)
print(*result)

# 8
# 1 -5 3 5 -4 -2 -4 5