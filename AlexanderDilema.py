import random
#Storing in an array all the six provided bills
drawn_bills = [10, 10, 10, 10, 10, 100]
Total_randombill = 0
Total_iteration = 0
#Validating the probability if Alexander goes with the proposed scheme of drawing random bills
for i in range(0, 10000):
    chance = random.choice(drawn_bills) + random.choice(drawn_bills)
    Total_randombill = Total_randombill + chance
    Total_iteration = i

Average_randombill = Total_randombill / Total_iteration
print("####### Scheme 1 #######")
print("The Average amount per month by drawing a random note for " + str(Total_iteration) + " months is ", Average_randombill)

#No need computation as other scheme gives a standard 50$ per month
print("\n####### Scheme 2 #######")
print("The confirmed Average amount per month is $50")
