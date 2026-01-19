import sys
import re
import random
import matplotlib.pyplot as plt
from Player import Player

#parsing the text file 
payoff_matrix = []
num_options = 0
game_name = ""

#helper method for creating the payoff matrix
def parse_matrix_line(line):
    banned_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:'"
    for char in line:
        if char in banned_chars: 
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
    return pair_list

#parsing file and creating payoff matrix
with open (sys.argv[1]) as file: 
    for line in file: 
        current_line = line
        if current_line[0] == "#":
            continue
        #set the all digit line as the number of options
        pattern_digits = r"^[0-9 ]+$"
        if re.match(pattern_digits, current_line):
            num_options = int(current_line)
            continue
        #set the all letter line as the name of the game
        pattern_letters = r"^[a-zA-Z ]+$"
        if re.match(pattern_letters, current_line):
            game_name = current_line
            continue
        else:
            row = parse_matrix_line(current_line)
            payoff_matrix.append(row)

#idk testing stuff
print("name:", game_name)
print("num_options:", num_options)
print("payoff matrix: ")
print(payoff_matrix)

#making all the players 
players = []
for i in range (10):
    name = i
    players.append(Player(name, num_options))

#round robin 
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

#running the simulations  
def simulate ():
    trials = 1000
    for i in range (trials):
        round_robin(players, payoff_matrix)
    for i in range (len(players)):
        print(players[i].get_prefs())
        
#plotting
def create_plot(p1_data, p2_data):
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

    ax.scatter(P1y, p1_x_vals, s=p1_sizes, c='blue', label='P1', alpha=0.3)
    ax.scatter(P2y, p2_x_vals, s=p2_sizes, c='orange', label='P2', alpha=0.4)

    # option two
    ax.set_xlabel('opera', fontsize=10)
    #options one
    ax.set_ylabel('football', fontsize=10)
    ax.set_title('battle of sexes')

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

    plt.legend([p1CollectionLegend, p2CollectionLegend], ['P1', 'P2'])

    plt.show()
    

simulate()
p1 = 0
p2 = 0
while p1 == p2: 
    p1 = random.randint(0, len(players))
    p2 = random.randint(0, len(players))
create_plot(players[p1].get_all_prefs()[0], players[p2].get_all_prefs()[0])

