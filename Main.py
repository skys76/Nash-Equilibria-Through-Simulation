import sys
import re

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


        



