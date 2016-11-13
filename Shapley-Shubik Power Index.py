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

def coalitions(player_list):
	'''Takes a list of player names
	and returns all a list of tuples of all possible coalitions.'''
	s = player_list
	list_of_coalitions = list(itertools.permutations(s,len(s)))
	return list_of_coalitions

def convert_to_number(list, dict):
	'''Takes list of players and uses dictionary to convert to a list
	of the players weights. Returns that list.'''
	number_list = []
	for i in list:
		number_list.append(dict[i])
	return number_list

def pivotal_players(list, dict, quota, player_scores):
	'''Takes a list of coalitions, a dictionary that converts players to their weights and finds the pivotal player. Returns dictionary with number of times each player is pivotal.'''
	total = 0
	pivotal_list = []
	for i in list:
		num_list = convert_to_number(i, dict)
		for j in range(len(num_list)):
			test_critical = num_list[j]
			total += test_critical
			if total >= quota:
				player_scores[i[j]] += 1
				total = 0
				pivotal_list.append(i[j])
				break
	return player_scores, pivotal_list

def find_ratios(dict):
	'''Takes a dictionary of players and number of time player is critical
	and prints each players ratio and percent of power.'''
	total_critical = sum(dict.values())
	for i in range(1,len(dict)+1):
		percent = dict["player " + str(i)]/total_critical * 100
		print("Player %s has %i/%i, or %.2f%% of the power" %(i,dict["player " + str(i)],total_critical,percent))
	return

def main():
	'''Calculates the Banzhaf Power Distribution of a weighted
	voting system.'''
	print()
	print("The Yaiko Shapley-Shubik Power Distribution Calculator")
	print("Version 1.1.7")
	print()
	quota, weights, player_list, player_score = get_data()
	coalition = coalitions(player_list)
	player_scores_dict, pivotal_list = pivotal_players(coalition,weights,quota,player_score)
	print()
	print("COALTIONS WITH PIVOTAL PLAYER")
	for i in range(len(coalition)):
		print(str(coalition[i]) + "     " + str(pivotal_list[i]))
	print()
	print("BANZHAF POWER INDEX")
	find_ratios(player_scores_dict)

main()
