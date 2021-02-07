import random

match = 0
no_match = 0
#Do it for 100000 trials
for _ in range(100000):
    birthdays = []
    #Trial performed over 25 people
    for _ in range(25):
        #Random function generates random integers
        random_birthday = random.randint(0, 365)
        birthdays.append(random_birthday)
        #Set function checks for duplicate entries and if not unique will be added to no_match birthdays
    if len(birthdays) == len(set(birthdays)):
        no_match += 1
    else:
        match += 1

print("Probability that at least 2 people with the same birthday in a group of 25 people is :",
      match / (match + no_match))
