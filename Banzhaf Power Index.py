import itertools

def get_data():
	weights = {}
	player_score = {}
	player_list = []
	quota = int(input("What is the quota for your voting system?\n"))
	number_of_players = int(input("How many players are in the system?\n"))
	for i in range(number_of_players):
		weight = int(input("What is the weight for player %s " %(i+1)))
		weights["player " + str(i+1)] = weight
		player_score["player " + str(i+1)] = 0
		player_list.append("player " + str(i+1))
	return quota, weights, player_list, player_score

def winning_coalitions(quota,weights,player_list):
	s = player_list
	winners = []
	for i in range(1,len(s)+1):
		x = list(itertools.combinations(s,i))
		for j in range(len(x)):
			check_list = convert_to_number(x[j],weights)
			total = sum(check_list)
			if total >= quota:
				winners.append(x[j])
	return winners
	
def convert_to_number(list, dict):
	'''Takes list of players and uses dictionary to convert to a list
	of the players weights. Returns that list.'''
	number_list = []
	for i in list:
		number_list.append(dict[i])
	return number_list

def critical_players(list, quota, player_scores):
	'''Takes a list of numbers, drops one at a time and checks
	if the sum is greater or equal to the quota.
	Returns dictionary with number of times each player is critcal.'''
	for i in range(len(list)):
		test_critical = list[i]
		del list[i]
		if sum(list) < quota:
			player_scores[test_critical] += 1
		list.insert(i, test_critical)	
		
	
a,b,c,d = get_data()
best = winning_coalitions(a,b,c)
sentence = " is a winning coaltion."
for i in range(len(best)):
	print(str(best[i]) + sentence)
print(b)
print(c)
#def critical_players(list):
	
