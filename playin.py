from Player import Player

player = Player("Sky", 5)
print("prefs: ", player.get_prefs())
print("current score: ", player.get_current_score())
print("total_score: ", player.get_total_score())
print("average_score: ", player.get_avg_score())
print("current_strat: ", player.get_current_strat())

#one round played
player.play(-3)
print("prefs: ", player.get_prefs())
print("current score: ", player.get_current_score())
print("total_score: ", player.get_total_score())
print("average_score: ", player.get_avg_score())
print("current_strat: ", player.get_current_strat())

#two rounds played
player.play(4)
print("prefs: ", player.get_prefs())
print("current score: ", player.get_current_score())
print("total_score: ", player.get_total_score())
print("average_score: ", player.get_avg_score())
print("current_strat: ", player.get_current_strat())
