now = time.time()
time_limit = 30
end_time = now + time_limit

while time.time() < end_time:
    time_remaining = end_time - time.time()
    print("You have {} seconds remaining".format(time_remaining))

while True:
    guess = input("What's your guess? ")
    if time.time() >= end_time:
        print("TIME IS UP")
        break
    if guess == answer:
        print("You got it!")
        break
