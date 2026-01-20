"""Project: Nash Equilibria Through Simulation
    
Author: Sky Stankevich 
Date: 1/20/2026

AI Usage: 
    ChatGPT was asked: 
        "how do different payoff matrices effect the convergence onto
        a Nash Equilibrium in the Stag and Hare game?"
        "explain regret-based learning" 
        "how could you use regret-based learning to reach a Nash equilibrium?" 

    Sources: None
"""
import sys
import re
import random
import matplotlib.pyplot as plt
from Player import Player

payoff_matrix = []
num_options = 0
game_name = ""
options = []


"""
def parse_matrix_line(line): when given a line read from a text file containing both letters and numbers, 
the method strips all letters from the string and seperates the numbers into a payoff matrix. 

Args: 
    line: string read from text file 
Returns: 
    pair_list: list returning the pairs of payoff scores read from the given line. This represents 
    one row of the payoff matrix. 
    start_string: the name of the option represented by the returned row in the payoff matrix 
"""
def parse_matrix_line(line):
    banned_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:'"
    start_string = ""
    for char in line:
        if char in banned_chars: 
            start_string = start_string + char
            line = line.replace(char, "")
    string_list = line.split(" ")
    clean_list = []
    for element in string_list:
        if element == "":
            continue
        else:
            clean_list.append(element)
    pair_list = []
    for i in range(0, (len(clean_list) - 1), 2):
        first = clean_list[i]
        second = clean_list[i+1]
        pair_list.append((first, second))
    return pair_list, start_string

#parsing file and creating payoff matrix
#opening text file
with open (sys.argv[1]) as file: 
    for line in file: 
        current_line = line
        #ignoring comments
        if current_line[0] == "#":
            continue
        #line containing only digits set as the number of options
        pattern_digits = r"^[0-9 ]+$"
        if re.match(pattern_digits, current_line):
            num_options = int(current_line)
            continue
        #line containing all letters set as the name of the game
        pattern_letters = r"^[a-zA-Z' ]+$"
        if re.match(pattern_letters, current_line):
            game_name = current_line
            continue
        #line containing both letters and numbers decoded by the helped "parse_matrix_line" method
        else:
            row = parse_matrix_line(current_line)[0]
            options.append(parse_matrix_line(current_line)[1])
            payoff_matrix.append(row)

#logging the game info 
print("Game name:", game_name)
print("Number of options:", num_options)
print("Moves: ", options[0], ", ", options[1])
print("Payoff Matrix: ")
print(payoff_matrix)

#make a list of players for the round robin using the Player class
players = []
for i in range (10):
    name = i
    players.append(Player(name, num_options))

"""
def round_robin(players, payoff): plays 45 games (1 round) using the players from the passed
list.
Args: 
    players: list of players in the round robin. Players' preferences remain no matter who they 
    play. 
    payoff: payoff matrix of the game, read from the text file.
Returns: 
    N/A
"""
def round_robin(players, payoff):
    p2_index = 1
    for p1 in players: 
        for j in range (p2_index, len(players)):
            p2 = players[p2_index]
            action1 = p1.get_current_strat()
            action2 = p2.get_current_strat()
            cell = payoff[action1][action2]
            p1_alt_cell = payoff[1-action1][action2]
            p2_alt_cell = payoff[action1][1-action2]
            p1.play(int(cell[0]), int(p1_alt_cell[0]))
            p2.play(int(cell[1]), int(p2_alt_cell[1]))
        if p2_index < len(players):
            p2_index = p2_index + 1
        else: 
            break

"""
def simulate(): uses the round_robin method to run 50 rounds of gameplay. 

Args: N/A
Returns: N/A
"""
def simulate ():
    trials = 50
    for i in range (trials):
        round_robin(players, payoff_matrix)
    for i in range (len(players)):
        print(players[i].get_prefs())
        
"""
def create_plot(p1_data, p2_data, p1_name, p2_name): plots the player's preferences over time using the 
size of data points to represent probability frequency. Taken from Mr. Sahu and modified to take more arguments 
and repeat all actions for two players, not one. 

Args: 
    p1_data: all of player 1's preferences over the 2250 games 
    p2_data: all of player 2's preferences over the 2250 games 

Returns: N/A
"""
def create_plot(p1_data, p2_data, p1_name, p2_name):
    p1stratsUnique = set(p1_data)
    p1_x_vals = list(p1stratsUnique)
    p1_sizes = []
    for i in range (len(p1_x_vals)):
        p1_sizes.append(p1_data.count(p1_x_vals[i]))

    p2stratsUnique = set(p2_data)
    p2_x_vals = list(p2stratsUnique)
    p2_sizes = []
    for i in range (len(p2_x_vals)):
        p2_sizes.append(p2_data.count(p2_x_vals[i]))

    P1y = []
    for P1xVal in p1_x_vals:
        P1y.append(1-P1xVal)

    P2y = []
    for P2xVal in p2_x_vals:
        P2y.append(1-P2xVal)

    fig, ax = plt.subplots()

    ax.scatter(P1y, p1_x_vals, s=p1_sizes, c='blue', label= p1_name, alpha=0.3)
    ax.scatter(P2y, p2_x_vals, s=p2_sizes, c='orange', label= p2_name, alpha=0.4)

    # option two
    ax.set_xlabel(options[1], fontsize=10)
    #options one
    ax.set_ylabel(options[0], fontsize=10)
    ax.set_title(game_name)

    # show grid
    ax.grid(True)

    p1LegendX = [0.5]
    p1LegendY = [0.5]
    p1LegendSize = [50]
    p1CollectionLegend = ax.scatter(p1LegendX, p1LegendY, s=p1LegendSize, c='blue', alpha=0.5)

    p2LegendX = [0.5]
    p2LegendY = [0.5]
    p2LegendSize = [50]
    p2CollectionLegend = ax.scatter(p2LegendX, p2LegendY, s=p2LegendSize, c='orange', alpha=0.4)

    plt.legend([p1CollectionLegend, p2CollectionLegend], [p1_name, p2_name])

    plt.show()
    

#running the 2250 rounds 
simulate()
#choosing two of the the ten player's whoes preferences will be graphed
p1 = 0
p2 = 0
while p1 == p2: 
    p1 = random.randint(0, len(players)-1)
    p2 = random.randint(0, len(players)-1)
    p1_name = f"player {p1+1}"
    p2_name = f"player {p2+1}"
#plot the chosen's player's preferences 
create_plot(players[p1].get_all_prefs()[0], players[p2].get_all_prefs()[0], p1_name, p2_name)


