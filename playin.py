"""import random
class Player:
    def __init__(self, name, num_options):
        self.name = name
        self.num_options = num_options
        self.current_score = 0
        self.alt_scores = []
        self.total_score = 0
        self.average_score = 0
        self.rounds_played = 0
        #by index in the prefs list
        self.current_strat = 0
        self.prefs = []
        for i in range(num_options):
            self.prefs.append(1/num_options)

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
        return self.alt_scores
    
    #FIRST updating stuff after one round
    def update_round(self, round_score, alt_scores):
        self.current_score = round_score
        self.rounds_played = self.rounds_played + 1
        self.total_score = self.total_score + round_score
        self.alt_scores = alt_scores

    #SECOND update the preferences 
    def update_prefs(self):
        change = 0
        for choice in self.alt_scores():
            change += max(0, choice - self.current_score)

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
        #print(self.name, self.prefs)
    
    #THIRD update the average 
    def update_average (self):
        self.average_score = self.total_score / self.rounds_played
    
    #FOURTH choose a new current strat
    def update_strat (self):
        num = random.random()
        sum = 0
        for i in range (len(self.prefs)):
            if sum < num and num < sum + self.prefs[i]:
                self.current_strat = i
                break 
            sum = sum + self.prefs[i]
    
    #cleaning it up
    def play (self, score, alt_scores):
        self.update_round(score, alt_scores)
        self.update_prefs()
        self.update_average()
        self.update_strat()
"""