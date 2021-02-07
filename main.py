# Library in python to return random integers
import random

# Keep track of where we are in experiment
statistics = {'match': 0, 'NoMatch': 0}
# Do the trials for 100 times for 25 people
for _ in range(100):
    birthdays = []  # List of birthday from 1 to 365
    for _ in range(23):
        randombirthday = random.randint(0, 365)  # Produce random integers
        birthdays.append(randombirthday)
        # Set is unique(does not hold the same value twice)
        if len(birthdays) == len(set(birthdays)):
            statistics['NoMatch'] += 1
        else:
            statistics['match'] += 1
        # Print the probability of the matches
        print("Probability that at least 2 in 25 people have same birthday is")
        print(statistics['match']/(statistics['match']+statistics['NoMatch']))