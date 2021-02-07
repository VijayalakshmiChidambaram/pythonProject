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
