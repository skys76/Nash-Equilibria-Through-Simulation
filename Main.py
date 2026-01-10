import sys
import re
#parsing the text file 
payoff_matrix = []
num_options = 0
game_name = ""


def parse_matrix_line(line):
    line = line.strip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    row = []
    #add the numbers as ordered pairs to the row but i'm too tired to do that rn
    return row


with open (sys.argv[1]) as file: 
    for line in file: 
        current_line = line
        if current_line[0] == "#":
            continue
        if re.match(r'^([\s\d]+)$', current_line):
            num_options = int(current_line)
        if re.match(r'^([\sa-zA-Z]+)$', current_line):
            game_name = current_line
        else:
            row = parse_matrix_line(current_line)
            payoff_matrix.append(row)



        

        



