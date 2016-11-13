import itertools

def get_data():
	'''Gets user input to assign a quota, a dictionary of players and their weights,
	a list of player names and a dictionary of player names assigned to their weights.'''
	weights = {}
	player_score = {}
	player_list = []
	quota = int(input("What is the quota for your voting system?\n"))
	number_of_players = int(input("How many players are in the system?\n"))
	for i in range(number_of_players):
		weight = int(input("State the weight for player %s: " %(i+1)))
		weights["player " + str(i+1)] = weight
		player_score["player " + str(i+1)] = 0
		player_list.append("player " + str(i+1))
	return quota, weights, player_list, player_score

def winning_coalitions(quota,weights,player_list):
	'''Takes a quota, dictionary of players and their weights and a list of player names
	and returns all a list of tuples of all possible winning coalitions.'''
	s = player_list
	winners = []
	x = list(itertools.permutations(s,len(s)))
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

quota, weights, player_list, player_score = get_data()
x = winning_coalitions(quota, weights, player_list)
print(len(x))
