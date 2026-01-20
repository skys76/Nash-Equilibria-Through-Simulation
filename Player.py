"""
Class: Player (self, name, num_options): creates a player object which plays against opponents in a 2 X 2 game. 
The player is able to learn strategies which gravitate towards the game's Nash equilibrium by updating their preferences 
for strategies based on the outcome of a single game."""
import random
class Player:
    def __init__(self, name, num_options):
        self.name = name
        self.num_options = num_options
        self.current_score = 0
        self.alt_score = 0
        self.total_score = 0
        self.average_score = 0
        self.rounds_played = 0
        #by index in the prefs list
        self.current_strat = 0
        self.prefs = []
        for i in range(num_options):
            self.prefs.append(1/num_options)
        self.all_prefs = [[], []]

    #getter methods 
    def get_prefs(self):
        return self.prefs
    def get_current_score(self):
        return self.current_score
    def get_total_score(self):
        return self.total_score
    def get_avg_score(self):
        return self.average_score
    def get_current_strat(self):
        return self.current_strat
    def get_name(self):
        return self.name
    def get_rounds_played(self):
        return self.rounds_played
    def get_alt_score(self):
        return self.alt_score
    def get_all_prefs(self): 
        return self.all_prefs
    
    """
  def update_round(self, round_score, alt_score): updates player's stats "after" a game is played (really there is no game being played, 
  by the player recives a score as if it is, so.)

  Args: 
    round_score: payoff from the current round 
    alt_score: while maintaining the opponent's chosen strategy, what score could the player have gotten if they played the strategy they 
    didn't choose?

    Returns: N/A
"""
    #FIRST 
    def update_round(self, round_score, alt_score):
        self.current_score = round_score
        self.rounds_played = self.rounds_played + 1
        self.total_score = self.total_score + round_score
        self.alt_score = alt_score

    """
    def update_prefs(self): updates preferences (which are in the form of probabilities) based on how much the player regrets using their 
    current strategy in the previous game. 
    
    Args: N/A
    
    Returns: N/A"""
    #SECOND 
    def update_prefs(self):
        change = self.alt_score - self.current_score
        for i in range(len(self.prefs)):
            if i == self.current_strat:
                self.prefs[i]-= change * .01
            else: 
                self.prefs[i] += (change * .01)/(self.num_options - 1)
                
        for i in range(len(self.prefs)): 
            if self.prefs[i] > 1:
                self.prefs[i] = 1
            elif self.prefs[i] < 0:
                self.prefs[i] = 0
            self.all_prefs[i].append(self.prefs[i])
    
    """def update_average(self): updates the player's average score
    
    Args: N/a
    
    Returns: N/a"""
    #THIRD 
    def update_average (self):
        self.average_score = self.total_score / self.rounds_played
    
    """
    def update_strat(self): A random number between 0 and 1 is chosen. Since the player's preferences for strategies are stored 
    as probabilities, the random number is used to determine which strategy will be played next round.
    
    Args: N/A
    
    Returns: N/A"""
    #FOURTH 
    def update_strat (self):
        num = random.random()
        sum = 0
        for i in range (len(self.prefs)):
            if sum < num and num < sum + self.prefs[i]:
                self.current_strat = i
                break 
            sum = sum + self.prefs[i]
    
    def round_all_prefs(self):
        for i in range (len(self.all_prefs)):
            for j in range(len(self.all_prefs[i])):
                self.all_prefs[i][j] = round(self.all_prefs[i][j], 2)
    
    """
    def play(self, score, alt_score): preforms all of the above methods in the correct order. 
    
    Args: 
        score: the payoff from playing one round using the player's current strategy 
        alt_score: 
        alt_score: while maintaining the opponent's chosen strategy, what score could the player have gotten if they played the strategy they 
        didn't choose?
    
    Returns: N/A
"""
    def play (self, score, alt_score):
        self.update_round(score, alt_score)
        self.update_prefs()
        self.update_average()
        self.update_strat()
        self.round_all_prefs()
