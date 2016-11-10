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

def critical_players(list, dict, quota, player_scores):
	'''Takes a list of players of winning coalitions, a dictionary that converts players to their weights and drops one player at a time and checks if the sum is greater or equal to the quota. Returns dictionary with number of times each player is critical.'''
	for i in list:
		num_list = convert_to_number(i, dict)
		for j in range(len(num_list)):
			test_critical = num_list[j]
			del num_list[j]
			if sum(num_list) < quota:
				player_scores[i[j]] += 1
			num_list.insert(j, test_critical)
	return player_scores
	
def find_ratios(dict):
	total_critical = sum(dict.values())
	for i in range(1,len(dict)+1):
		percent = dict["player " + str(i)]/total_critical * 100
		print("Player %s has %i/%i, or %.2f percent of the power" %(i,dict["player " + str(i)],total_critical,percent))
	return "Goodbye."

a,b,c,d = get_data()
best = winning_coalitions(a,b,c)
#sentence = " is a winning coaltion."
#for i in range(len(best)):
#	print(str(best[i]) + sentence)

player_scores = critical_players(best,b,a,d)
print(find_ratios(player_scores))
