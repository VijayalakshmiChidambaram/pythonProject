Problem Statement 1:
What is the probability that in a randomly selected group of N people (say N=25 people), there will be at least 2 people with the same birthday?

# pythonProject
Solving Birtday Paradox

Pseudocode :
Match = 0
No_Match =0
For I in range of trials
Birthdays[]
For j in range of number of people
		Random.rand_int[0,365]
		Append to Birthdays[]
If no duplicate entries
	No_Match +=1
Else
	Match +=1
Print Probability [Match /( Match + No_Match)]
END

Output :
Probability that at least 2 people with the same birthday in a group of 25 people is : 0.56865

Explanation :
On performing the given functionality to obtain the probability that in a randomly selected group of N people (say N=25) with at least 2 people with the same birthday the computer simulated output was obtained to be around 50 %
Here I considered a large data set with the number of trials to be 100000, with each trial running over 25 people. I used the rand_int function to generate random birthday dates and applied the set function to look for unique birthday match and the probability was computed.

Problem Statement 2:
Alexendar’s Dilemma - I owe my son Alexander $50 per month for doing chores around the house. Instead of giving him the $50, each month I will let him reach into a bag which contains a $100 bill and five $10 bills, and draw two of the bills. Should Alexander go with this scheme, or in other words, is my scheme fair? If Alexander is a risk taker, then he will have a chance of making $110 instead of $50 per month if he is lucky. On the other hand, if he is risk averse, then he figures that he will more likely be getting $20 rather than $50 per month. So the question is: In the long run, will he be better off taking the $50 or go with my scheme?

Pseudocode :
	Initialize and array of six provided bills
	For I in range [0, N trials]:
		Random.choice over six bills
		Store the value
		Retrieve a mean value
	End For loop
	Print the average value for N trials over six bills
	Print the standard bill result of 50$
END the program

Output :
####### Scheme 1 #######
The Average amount per month by drawing a random note for 9999 months is  50.55105510551055

####### Scheme 2 #######
The confirmed Average amount per month is $50

Explanation :
As per my observation over computer simulation both the schemes produced the same results for large data set (say 10000 trials). So, Alexander can go with choosing any of the two schemes for the long run.
For the first scheme of drawing from , I considered a list of six bills and used the random choice function to compute the total and average value for N trials (N = 10000).
In the second scheme for taking 50 $ each month no computation is required, as it is known that giving a standard amount of 50$ each month for N times will yield the same 50$.
Hence, both schemes yield the same amount of 50$ per month on an average to alexander in the long run.
