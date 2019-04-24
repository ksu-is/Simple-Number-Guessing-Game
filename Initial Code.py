
from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Please guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum possible value is: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "You may not guess higher than the maximum value!"
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
      print "Congrats, you have won the game!"
      return
    else:
      print "Sorry, you have lost the game!!"
      return
