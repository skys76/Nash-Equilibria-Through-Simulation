import sys
import re
#parsing the text file 
payoff_matrix = []
num_options = 0
game_name = ""

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

with open (sys.argv[1]) as file: 
    for line in file: 
        current_line = line
        if current_line[0] == "#":
            continue
        #basically trying to eliminate the only letter and only string lines. 
        #but it's not working 
        if re.match(r'^([\s\d]+)$', current_line):
            num_options = int(current_line)
        if re.match(r'^([\sa-zA-Z]+)$', current_line):
            game_name = current_line
        else:
            row = parse_matrix_line(current_line)
            payoff_matrix.append(row)

    
print("name:", game_name)
print("num_options:", num_options)
print("payoff matrix: ")
print(payoff_matrix)
        



