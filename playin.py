import re
def parse_matrix_line(line):
    banned_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:'"
    for char in line:
        if char in banned_chars: 
            line = line.replace(char, "")
    print(line)
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

line = "row: 2 2 -9 -10"
print(parse_matrix_line(line))

