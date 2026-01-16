#simple case with only two players. IT WORKS!
from Player import Player 

p1 = Player("p1", 2)
p2 = Player("p2", 2)

payoff_matrix = [[('-1', '-1'), ('0', '-10\n')], 
                 [('-10', '0'), ('-6', '-6')]]
for i in range (5000):
    cell = payoff_matrix[p2.get_current_strat()][p1.get_current_strat()]
    p1.play(int(cell[0]))
    p2.play(int(cell[1]))

print(p1.get_prefs())
print(p2.get_prefs())


"""
payoff_matrix = [[('10', '10'), ('0', '0\n')], 
                 [('0', '0'), ('0', '0')]]

output: [1, 0]
        [1, 0]

payoff_matrix = [[('10', '0'), ('8', '0\n')], 
                 [('6', '0'), ('4', '0')]]

output: [0.8598682037462457, 0.1401317962537543]
        [0, 1]
"""