import sys
import re
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
for i in range (2):
    name = i
    players.append(Player(name, num_options))

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
    
def simulate ():
    trials = 1000
    for i in range (trials):
        round_robin(players, payoff_matrix)
    for i in range (len(players)):
        print(players[i].get_prefs())
simulate()
        

