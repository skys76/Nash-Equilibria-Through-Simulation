import random
class Player:
    def __init__(self, name, num_options):
        self.name = name
        self.num_options = num_options
        self.current_score = 0
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
    
    #FIRST updating stuff after one round
    def update_round(self, round_score):
        self.current_score = round_score
        self.rounds_played = self.rounds_played + 1
        self.total_score = self.total_score + round_score

    #SECOND update the preferences 
    def update_prefs(self):
        #three cases
        delta_pref = .01
        delta_remove = delta_pref/(self.num_options - 1)

        #current score is greater than the average = win 
        if self.current_score > self.average_score:
            for i in range(len(self.prefs)):
                if i == self.current_strat:
                    self.prefs[i] = self.prefs[i] + delta_pref
                else: 
                    self.prefs[i] = self.prefs[i] - delta_remove
        #current score is less than the average = loss 
        if self.current_score  < self.average_score:
            for i in range(len(self.prefs)):
                if i == self.current_strat:
                    self.prefs[i] = self.prefs[i] - delta_pref
                else: 
                    self.prefs[i] = self.prefs[i] + delta_remove
        #current score is equal to the average = do nothing 
    
    #THIRD update the average 
    def update_average (self):
        self.average_score = self.total_score / self.rounds_played
    
    #FOURTH choose a new current strat
    def update_strat (self):
        num = random.random()
        print("random number is: ", num)
        sum = 0
        for i in range (len(self.prefs)):
            if sum < num and num < sum + self.prefs[i]:
                self.current_strat = i
                break 
            sum = sum + self.prefs[i]
    
    #cleaning it up
    def play (self, score):
        self.update_round(score)
        self.update_prefs()
        self.update_average()
        self.update_strat()
