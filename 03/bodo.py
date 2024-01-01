# n=int(input())

# # Read the number of players 
# n = int(input()) # Create a list to store players' positions
# positions = [] 
# # Read the player information 
# for _ in range(n): 
#     step, path = input().split() 
#     position = step + path 
#     positions.append(position) 
# # Sort the positions in descending order 
# positions.sort(reverse=True) 
# # Generate and print the rankings 
# rankings = {} 
# for i, position in enumerate(positions, start=1): 
#     player = position.strip('.|') 
#     rankings[i] = player 
# # Print the final rankings 
# for rank, player in rankings.items(): 
#     print(f"{rank}: {player}")




n = int(input()) 
player_positions = {} 
for _ in range(n): 
    line = input().split() 
    steps = int(line[0]) 
    path = line[1] 
position = path.rfind('|') + 1 
if position in player_positions:
    player_positions[position].append(path[steps]) 
else: player_positions[position] = [path[steps]] 
sorted_players = sorted(player_positions.items()) 
rank = 1 
for _, players in sorted_players:
    print(f"{rank}: {' '.join(players)}") 
    rank += len(players)