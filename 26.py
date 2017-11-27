winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

def check_winner(table):
	
	for player in [1,2]:
		for index in [0,1,2]:
			'''
			if len(set( [table[index][x] for x in [0,1,2]] )) == 1:
				return player
			if len(set( [table[x][index] for x in [0,1,2]] )) == 1:
				return player
			'''
			if len(filter(lambda x: table[index][x] == player, [0,1,2])) == 3:
				return player
			if len(filter(lambda x: table[x][index] == player, [0,1,2])) == 3:
				return player
			
	if table[0][0] == table[1][1] == table[2][2]:
		return table[1][1]
	if table[0][2] == table[1][1] == table[2][0]:
		return table[1][1]

print check_winner(winner_is_2)
print check_winner(winner_is_1)
print check_winner(winner_is_also_1)
print check_winner(no_winner)
print check_winner(also_no_winner)
