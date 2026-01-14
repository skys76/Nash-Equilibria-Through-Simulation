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
            self.prefs.append(.5)

    #updating stuff after one round
    def update_round(self, round_score):
        self.current_score = round_score
        self.rounds_played = self.rounds_played + 1
        self.total_score = self.total_score + round_score

    #update the average (happnes AFTER you update the preferences)
    def update_average (self):
        self.average_score = self.total_score / self.rounds_played

    def update_prefs(self):
        #three cases
        delta_pref = .01
        delta_remove = (1-delta_pref)/(self.num_options - 1)

        #current score is greater than the average = win 
        if self.current_score > self.average_score:
           

        #current score is less than the average = loss 
        if self.current_score  < self.average_score:
            
        #current score is equal to the average = do nothing 
        
