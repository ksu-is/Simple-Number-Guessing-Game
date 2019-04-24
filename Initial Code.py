"""
This is a program that rolls a pair of dice and asks the user to guess a number. Based on the user's guess, the program should determine a winner. If the user's guess is greater than the total value of the dice roll, they win! Otherwise, the computer wins.
The program does the following:
1. Randomly rolls a pair of dice
2. Adds the values of the roll
3. Asks the user to guess a number
4. Compares the user's guess to the total value
5. Decides a winner (the user or the program)
6. Informs the user who the winner is.
"""
from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum possible value is: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "No guessing higher than the maximum possible value!"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The first value is %d" % first_roll
    sleep(1)
    print "The second value is %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total value is %d" % total_roll
    sleep(1)
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "You have won!"
      return
    else:
      print "You have lost!"
      return
