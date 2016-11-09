import itertools

def get_data():
	weights = []
	quota = int(input("What is the quota for your voting system?\n"))
	number_of_players = int(input("How many players are in the system?\n"))
	for i in range(number_of_players):
		weight = int(input("What is the weight for player %s " %(i+1)))
		weights.insert(i,weight)
	return quota, weights

def winning_coalitions(quota,weights):
	s = weights
	winners = []
	for i in range(1,len(s)+1):
		x = list(itertools.combinations(s,i))
		for j in range(len(x)):
			total = [sum(x[j])]
			if total[0] >= quota:
				winners.append(x[j])
	return winners
	
a,b = get_data()
best = winning_coalitions(a,b)
sentence = " is a winning coaltion."
for i in range(len(best)):
	print(str(best[i]) + sentence)
	
#def critical_players(list):
	
