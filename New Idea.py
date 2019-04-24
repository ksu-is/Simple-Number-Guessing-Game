import random

give_number = input("We will roll a 6 sided dice. What do you think the number will be?\n ")
guess_number = 1

dice = random.randint(1,6)
while give_number != dice:
    if give_number > dice:
        give_number = input("Sorry, that answer is too high! Try again!\n ")
        guess_number = guess_number +1
    if give_number < dice:
        give_number = input("Sorry, that answer is too low! Try again!\n ")
        guess_number = guess_number +1

print "Congratulations, you were right, the answer was {}! It took you {} tries.".format(dice, guess_number)
